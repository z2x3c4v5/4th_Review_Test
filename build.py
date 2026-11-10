"""Build index.html: inline images/ into app.html as data URIs (single self-contained file)."""
import base64, json, pathlib
root = pathlib.Path(__file__).parent
imgs = {f.stem: "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()
        for f in sorted((root / "images").glob("*.jpg"))}
html = (root / "app.html").read_text(encoding="utf-8")
html = html.replace("/*__IMAGES__*/", "window.IMG = " + json.dumps(imgs) + ";")
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB,", len(imgs), "images")
