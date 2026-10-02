"""Run with: python verify.py (no dependencies)."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "https://spplastindustries.com", "https://mamtadesignco.com",
    "https://studiorei.art", "https://www.magnushathaway.com",
    "https://agproject.io", "https://asambhav.in", "https://chainlabs.in",
    "https://www.playheadsup.xyz/game", "https://www.wits.academy",
    "https://www.prathamchudasama.com", "https://dycot.chainlabs.in",
    "https://app.sitesgpt.in", "https://tutorials-gym-crm.vercel.app",
}


def check_asset(source, parent=ROOT):
    url = urlsplit(source)
    if not url.scheme and not url.netloc:
        assert (parent / url.path).is_file(), f"Missing local asset: {source}"


class PageCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.projects = []
        self.categories = Counter()
        self.stylesheets = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        assert tag != "script", "This example must remain HTML and CSS only"
        if "project-row" in attrs.get("class", "").split():
            assert tag == "a", "Every project row must be a link"
            self.projects.append(attrs["href"].rstrip("/"))
            self.categories.update(attrs.get("data-category", "").split())
        if tag == "img":
            check_asset(attrs["src"])
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            check_asset(attrs["href"])
            self.stylesheets.append(attrs["href"])


page = PageCheck()
page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
assert len(page.projects) == len(set(page.projects)), "Duplicate project rows"
assert set(page.projects) == EXPECTED, "Project URLs differ from the supplied list"
assert page.categories == Counter(web=9, **{"3d": 4}, saas=4), page.categories
assert "styles.css" in page.stylesheets, "Local stylesheet must be linked"
css = (ROOT / "styles.css").read_text(encoding="utf-8")
for source in re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", css):
    check_asset(source.strip())
print("PASS: 13 unique project links; categories web=9, 3d=4, saas=4; local assets exist; no scripts.")
