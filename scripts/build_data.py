"""Curate the scraped social data into small JSON files + locally hosted thumbnails.
Usage: python -I scripts/build_data.py "<path to jeffrey data folder>"
Only verified numbers from the scrape are used. Instagram CDN images expire, so IG is
used for counts and permalinks only; YouTube thumbnails are downloaded and self-hosted.
"""
import sys, json, glob, os, re, io, urllib.request
from PIL import Image

src = sys.argv[1]
def load(pat): return json.load(open(glob.glob(os.path.join(src, pat))[0], encoding="utf8"))
yt, ig, fb = load("*youtube*"), load("*instagram*"), load("*facebook*")

def clean(t):
    t = re.sub(r"#\S+", "", t or "")
    t = re.sub(r"[^\x00-\x7F]+", " ", t)          # strip emoji / broken glyphs
    t = re.sub(r"\s*[|/]+\s*$", "", t)
    return re.sub(r"\s+", " ", t).strip(" .|-")

ch = yt[0]
channel = {"name": ch["channelName"], "handle": ch["channelUsername"], "url": "https://www.youtube.com/@" + ch["channelUsername"],
           "subscribers": ch["numberOfSubscribers"], "totalViews": ch["channelTotalViews"],
           "videos": ch["channelTotalVideos"], "joined": ch["channelJoinedDate"]}

def vid(v):
    return {"id": re.sub(r".*(?:v=|shorts/)", "", v["url"]), "title": clean(v["title"]) or "Jeffrey Nortey",
            "views": v["viewCount"], "duration": v.get("duration"), "short": v["type"] == "shorts",
            "url": v["url"], "thumb": v["thumbnailUrl"],
            "brandSafe": not re.search(r"nyash|buttock|bedroom|side-?chick|down there|slave|wifee|sex", v["title"], re.I)}

pool = [vid(v) for v in yt if v.get("viewCount")]
long_top = sorted([v for v in pool if not v["short"]], key=lambda v: -v["views"])[:12]
short_top = sorted([v for v in pool if v["short"]], key=lambda v: -v["views"])[:8]

os.makedirs("public/media/yt", exist_ok=True)
for v in long_top + short_top:
    out = f"public/media/yt/{v['id']}.jpg"
    if not os.path.exists(out):
        try:
            data = urllib.request.urlopen(urllib.request.Request(v["thumb"], headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read()
            im = Image.open(io.BytesIO(data)).convert("RGB"); im.thumbnail((960, 960))
            im.save(out, "JPEG", quality=78, optimize=True)
        except Exception as e:
            print("thumb fail", v["id"], e)
    v["thumb"] = f"/media/yt/{v['id']}.jpg"

# Instagram: permalinks + counts only (images expire)
mine = [p for p in ig if p["ownerUsername"] == "jeffreynortey1"]
vibes = [p for p in ig if p["ownerUsername"] == "vibesthemovie"]
def igp(p): return {"url": p["url"], "views": p.get("videoViewCount"), "likes": p.get("likesCount"), "caption": clean(p.get("caption"))[:140]}
ig_top = [igp(p) for p in sorted(mine, key=lambda p: -(p.get("videoViewCount") or 0))[:8]]
vibes_posts = [igp(p) for p in sorted(vibes, key=lambda p: -(p.get("videoViewCount") or 0))[:4]]
fb_top = [{"url": p["url"], "likes": p.get("likes"), "text": clean(p.get("text"))[:120]}
          for p in sorted(fb, key=lambda p: -(p.get("likes") or 0))[:6] if p.get("url")]

stats = {"ytSubscribers": ch["numberOfSubscribers"], "ytViews": ch["channelTotalViews"], "ytVideos": ch["channelTotalVideos"],
         "igPostsScraped": len(mine), "fbPostsScraped": len(fb)}
json.dump({"channel": channel, "long": long_top, "shorts": short_top, "ig": ig_top, "vibes": vibes_posts, "fb": fb_top, "stats": stats},
          open("src/data/social.json", "w", encoding="utf8"), indent=1, ensure_ascii=False)
print("ok", len(long_top), len(short_top), len(ig_top), len(vibes_posts), len(fb_top), channel["subscribers"])
