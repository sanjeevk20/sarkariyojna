"""Make docs/site/geo/districts.json: simplified district outlines for the states the site covers.

Source: DataMeet "Districts/Census_2011/2011_Dist" shapefile, CC BY 4.0,
https://github.com/datameet/maps (attribution shown on the map page).
Run once when boundaries or states change (needs the pure-Python `pyshp` package):

    python3 docs/site/build_geo.py /path/to/2011_Dist
"""
import json, pathlib, sys
import shapefile  # pyshp

STATES = {"Maharashtra": "mh", "Uttar Pradesh": "up", "Karnataka": "ka"}
TOL = 0.012      # simplification tolerance in degrees (about 1 km)
DIGITS = 3       # coordinate rounding (about 100 m)
OUT = pathlib.Path(__file__).resolve().parent / "geo" / "districts.json"


def dp(pts, tol):
    """Douglas-Peucker line simplification, iterative. A closed ring is split at the vertex farthest
    from its start, because start and end coincide and every distance to that 'line' would be zero."""
    if len(pts) < 4:
        return pts
    if pts[0] == pts[-1]:
        x0, y0 = pts[0]
        k = max(range(len(pts)), key=lambda i: (pts[i][0] - x0) ** 2 + (pts[i][1] - y0) ** 2)
        if 0 < k < len(pts) - 1:
            return dp(pts[:k + 1], tol)[:-1] + dp(pts[k:], tol)
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        (x1, y1), (x2, y2) = pts[a], pts[b]
        dx, dy = x2 - x1, y2 - y1
        norm = (dx * dx + dy * dy) ** 0.5 or 1e-12
        far, idx = 0.0, None
        for i in range(a + 1, b):
            x0, y0 = pts[i]
            d = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / norm
            if d > far:
                far, idx = d, i
        if idx is not None and far > tol:
            keep[idx] = True
            stack += [(a, idx), (idx, b)]
    return [p for p, k in zip(pts, keep) if k]


def rings(shape):
    parts = list(shape.parts) + [len(shape.points)]
    for s, e in zip(parts, parts[1:]):
        ring = dp(shape.points[s:e], TOL)
        ring = [[round(x, DIGITS), round(y, DIGITS)] for x, y in ring]
        dedup = [p for i, p in enumerate(ring) if i == 0 or p != ring[i - 1]]
        if len(dedup) >= 4:
            yield dedup


def main(src):
    r = shapefile.Reader(src)
    out = []
    for sr in r.iterShapeRecords():
        name, state, _, _, code = sr.record
        state = state.strip()
        if state not in STATES:
            continue
        rs = list(rings(sr.shape))
        if rs:
            out.append({"name": name.strip(), "state": STATES[state], "code": int(code), "rings": rs})
    out.sort(key=lambda d: (d["state"], d["name"]))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"source": "DataMeet India community, Census 2011 districts, CC BY 4.0",
                               "districts": out}, separators=(",", ":"), ensure_ascii=False))
    print(f"{len(out)} districts -> {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main(sys.argv[1])
