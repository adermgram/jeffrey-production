"""Trace the client's logo PNG (alpha channel) into clean SVG paths using potrace."""
import sys, numpy as np
from PIL import Image
import potrace

def trace(alpha, thresh=128):
    bm = potrace.Bitmap(~(alpha > thresh))  # potrace fills the False pixels in this binding
    plist = bm.trace(turdsize=20, alphamax=1.0, opttolerance=0.4)
    d = []
    for c in plist:
        s = c.start_point
        d.append(f"M{s.x:.1f},{s.y:.1f}")
        for seg in c.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
            else:
                d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        d.append("Z")
    return "".join(d)

def make(src, out, crop_x=None):
    a = np.array(Image.open(src).convert("RGBA").getchannel("A"))
    ys, xs = np.where(a > 128)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    if crop_x:  # monogram only: keep columns left of crop_x
        sub = a[:, :crop_x]
        ys, xs = np.where(sub > 128)
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        a = sub
    a = a[y0:y1+1, x0:x1+1]
    h, w = a.shape
    d = trace(a)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="Jeffrey Nortey Productions">'
           f'<path fill="currentColor" fill-rule="evenodd" d="{d}"/></svg>')
    open(out, "w", encoding="utf8").write(svg)
    print(out, w, h, len(svg)//1024, "KB")

if __name__ == "__main__":
    src = sys.argv[1]
    make(src, "public/brand/logo.svg")
    make(src, "public/brand/mark.svg", crop_x=int(4167*(700/1932)))
