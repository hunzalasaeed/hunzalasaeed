# -*- coding: utf-8 -*-
"""Static site generator for the portfolio.  Usage:  python src/build.py
Output goes to dist/ (upload the contents of dist/ to any web host)."""
import json, os, shutil, sys, datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import data as D  # noqa: E402

DIST = ROOT / "dist"
SITE = D.SITE_URL.rstrip("/")
TODAY = datetime.date.today().isoformat()
import time
VER = str(int(time.time()))
VIDEO_DIR = ROOT / "assets" / "video"

env = Environment(loader=FileSystemLoader(str(HERE / "templates")), autoescape=select_autoescape(["html"]),
                  trim_blocks=True, lstrip_blocks=True)
env.globals["m"] = env.get_template("_m.html").module


def absu(path):
    return f"{SITE}{path}" if SITE else None


def jsonld(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


projects = D.PROJECTS
# sites where FAQPage schema was found on the live homepage (checked Nov 2026)
FAQ_SCHEMA = {"fort-erie-pit-stop", "advance-therapy-canada", "advance-therapy-uk", "ontario-aba-therapy", "bajwa-cpa",
              "autaq-banquet-hall", "aba-therapy-toronto", "aba-therapy-mississauga", "advance-academy"}
for i, p in enumerate(projects):
    p["url"] = f"/work/{p['slug']}/"
    p["live"] = f"https://{p['domain']}/"
    p["scope_key"] = "seo-dev" if p["scope"] == D.SEO_DEV else "dev"
    p["thumb"] = f"/assets/img/thumbs/{p['slug']}.webp"
    p["shot"] = f"/assets/img/shots/{p['slug']}.webp"
    p["has_shot"] = (ROOT / "assets/img/shots" / f"{p['slug']}.webp").exists()
    p["next"] = projects[(i + 1) % len(projects)]
    p.setdefault("gsc", [])
    p["faq"] = p["slug"] in FAQ_SCHEMA

videos = []
for v in D.VIDEOS:
    f = VIDEO_DIR / f"{v['slug']}.mp4"
    if not f.exists():
        continue
    v = dict(v)
    v["src"] = f"/assets/video/{v['slug']}.mp4"
    v["poster"] = f"/assets/video/{v['slug']}.jpg"
    v["date"] = datetime.date.fromtimestamp(f.stat().st_mtime).isoformat()
    videos.append(v)
vmap = {v["slug"]: v for v in videos}
for p in projects:
    p["video_objs"] = [vmap[s] for s in p["videos"] if s in vmap]

person_ld = {
    "@type": "Person", "@id": (absu("/#person") or "#person"), "name": D.PERSON["name"], "jobTitle": D.PERSON["title"],
    "email": f"mailto:{D.PERSON['email']}", "telephone": D.PERSON["phone_e164"],
    "address": {"@type": "PostalAddress", "addressLocality": D.PERSON["locality"], "addressCountry": D.PERSON["country"]},
    "sameAs": [D.PERSON["linkedin"]],
    "knowsAbout": ["Search Engine Optimization", "Answer Engine Optimization", "Generative Engine Optimization", "Local SEO",
                   "Google Business Profile", "Technical SEO", "Schema Markup", "WordPress", "Elementor", "WooCommerce",
                   "Shopify", "Video Editing", "Motion Graphics", "Adobe Premiere Pro", "Adobe After Effects"],
}
if SITE:
    person_ld["url"] = SITE + "/"
    person_ld["image"] = SITE + "/assets/img/og.png"


def photo_info():
    f = ROOT / "assets/img/profile.webp"
    if not f.exists():
        return None
    from PIL import Image
    w, h = Image.open(f).size
    return {"src": "/assets/img/profile.webp", "w": w, "h": h}


def page_ctx(path, title, desc, og_image=None, **kw):
    return dict(photo=photo_info(), ver=VER, D=D, P=D.PERSON, path=path, title=title, desc=desc, canonical=absu(path),
                og_image=absu(og_image or "/assets/img/og.png"), site=SITE, year=datetime.date.today().year,
                projects=projects, videos=videos, jsonld=jsonld, **kw)


def write(path, html):
    out = DIST / path.lstrip("/")
    if path.endswith("/"):
        out = out / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def make_assets():
    """favicon, touch icon, OG image, and screenshots dropped into assets/img/raw/<slug>.png|jpg"""
    from PIL import Image, ImageDraw, ImageFont
    img = ROOT / "assets" / "img"
    (img / "shots").mkdir(parents=True, exist_ok=True); (img / "thumbs").mkdir(exist_ok=True)
    raw = img / "raw"
    if raw.exists():
        for f in raw.iterdir():
            if f.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
                continue
            im = Image.open(f).convert("RGB")
            w = min(1200, im.width); h = round(im.height * w / im.width)
            im = im.resize((w, h), Image.LANCZOS).crop((0, 0, w, min(h, 2500)))
            im.save(img / "shots" / f"{f.stem}.webp", quality=74, method=6)
            im.resize((min(800, w), round(im.height * min(800, w) / w)), Image.LANCZOS).save(img / "thumbs" / f"{f.stem}.webp", quality=70, method=6)
    (img / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#D4FF3A"/>'
        '<text x="32" y="42" font-family="Arial,Helvetica,sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#0B0C08">HS</text></svg>', encoding="utf-8")
    fb = "C:/Windows/Fonts/segoeuib.ttf"; fr = "C:/Windows/Fonts/segoeui.ttf"; fi = "C:/Windows/Fonts/georgiai.ttf"
    F = lambda path, size: ImageFont.truetype(path, size) if Path(path).exists() else ImageFont.load_default()
    t = Image.new("RGB", (180, 180), "#D4FF3A"); d = ImageDraw.Draw(t)
    d.text((90, 92), "HS", font=F(fb, 78), fill="#0B0C08", anchor="mm"); t.save(img / "apple-touch-icon.png")
    og = Image.new("RGB", (1200, 630), "#08090D"); d = ImageDraw.Draw(og)
    for r in range(380, 0, -4):
        a = int(26 * (1 - r / 380)); d.ellipse((900 - r, 120 - r, 900 + r, 120 + r), fill=(8 + a, 9 + a // 2, 13 + a * 2))
    d.rounded_rectangle((70, 70, 150, 150), 22, fill="#D4FF3A"); d.text((110, 112), "HS", font=F(fb, 36), fill="#0B0C08", anchor="mm")
    d.text((70, 215), "Get found.", font=F(fb, 92), fill="#F3F1EA")
    d.text((70, 320), "Get cited.", font=F(fi, 96), fill="#D4FF3A")
    d.text((70, 430), D.PERSON["name"], font=F(fb, 40), fill="#F3F1EA")
    d.text((70, 485), "SEO, AEO & GEO Specialist · WordPress Developer · Video Editor", font=F(fr, 29), fill="#9A9AA5")
    d.text((70, 540), "25+ websites · 25+ Google Business Profiles · 5 countries", font=F(fr, 26), fill="#D4FF3A")
    og.save(img / "og.png", optimize=True)
    # profile photo: put your original as assets/img/profile-original.(jpg|png|webp); it is only resized, never retouched
    for ext in ("jpg", "jpeg", "png", "webp"):
        src = img / f"profile-original.{ext}"
        if src.exists():
            im = Image.open(src).convert("RGB")
            w = min(900, im.width); h = round(im.height * w / im.width)
            im.resize((w, h), Image.LANCZOS).save(img / "profile.webp", quality=82, method=6)
            break


def build():
    make_assets()
    for p in projects:
        p["has_shot"] = (ROOT / "assets/img/shots" / f"{p['slug']}.webp").exists()
    DIST.mkdir(exist_ok=True)
    for child in DIST.iterdir():  # empty dist/ but keep the folder (a preview server may be using it)
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("raw", "profile-original.*"))
    if photo_info() and SITE:
        person_ld["image"] = SITE + "/assets/img/profile.webp"
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in D.FAQ]}

    # ---- home
    graph = [person_ld,
             {"@type": "WebSite", "name": f"{D.PERSON['name']} Portfolio", **({"url": SITE + "/"} if SITE else {}), "publisher": {"@id": person_ld["@id"]}},
             {"@type": "ProfilePage", "mainEntity": {"@id": person_ld["@id"]}, "name": f"{D.PERSON['name']}: {D.PERSON['title']}"},
             faq_ld,
             {"@type": "ItemList", "name": "Website projects", "itemListElement": [
                 {"@type": "ListItem", "position": n + 1, "name": p["name"], **({"url": SITE + p["url"]} if SITE else {})} for n, p in enumerate(projects)]}]
    if SITE:
        for v in videos:
            graph.append({"@type": "VideoObject", "name": f"{v['brand']}: {v['title']}", "description": f"{v['kind']} edited by {D.PERSON['name']} for {v['brand']}.",
                          "thumbnailUrl": SITE + v["poster"], "contentUrl": SITE + v["src"], "uploadDate": v["date"], "creator": {"@id": person_ld["@id"]}})
    ctx = page_ctx("/", f"{D.PERSON['name']} | SEO, AEO & GEO Specialist & WordPress Developer",
                   "SEO, AEO & GEO specialist, WordPress developer and video editor. 25+ client websites and 25+ Google Business "
                   "Profiles optimized across 5 countries.",
                   ld={"@context": "https://schema.org", "@graph": graph},
                   featured=[p for p in projects if p["featured"]], services=D.SERVICES)
    write("/", env.get_template("home.html").render(**ctx))

    # ---- work index
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": "Website projects", "about": {"@id": person_ld["@id"]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", **({"item": SITE + "/"} if SITE else {})},
            {"@type": "ListItem", "position": 2, "name": "Work", **({"item": SITE + "/work/"} if SITE else {})}]}]}
    write("/work/", env.get_template("work.html").render(**page_ctx(
        "/work/", f"Work: {len(projects)} Website, SEO & Development Projects | {D.PERSON['name']}",
        f"{len(projects)} live website projects: SEO and WordPress development for clinics, auto shops, accountants, "
        "event venues and more in 5 countries.", ld=ld)))

    # ---- case studies
    for p in projects:
        crumbs = [("Home", "/"), ("Work", "/work/"), (p["name"], p["url"])]
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "CreativeWork", "name": f"{p['name']} website", "about": p["industry"], "url": p["live"],
             "creator": {"@id": person_ld["@id"]}, "keywords": ", ".join([p["scope"], p["platform"], p["industry"]]),
             **({"image": SITE + p["shot"]} if SITE and p["has_shot"] else {})},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": n + 1, "name": name, **({"item": SITE + u} if SITE else {})} for n, (name, u) in enumerate(crumbs)]}]}
        where = f" in {p['location'].split(' · ')[0]}" if p["location"] else ""
        desc = f"{p['scope']} case study: {p['name']}, a {p['industry'].lower()} business{where}, built on {p['platform']}."
        if len(desc) < 125:
            desc += " See the live site and the work done."
        if len(desc) > 160:
            desc = f"{p['scope']} case study: {p['name']}, {p['industry'].lower()}, built on {p['platform']}. See the live site and work done."
        write(p["url"], env.get_template("case.html").render(**page_ctx(
            p["url"], f"{p['name']} Case Study: {p['scope']} | {D.PERSON['name']}", desc[:300],
            og_image=p["shot"] if p["has_shot"] else None, ld=ld, p=p)))

    # ---- 404
    write("/404.html", env.get_template("404.html").render(**page_ctx("/404.html", "Page not found | " + D.PERSON["name"], "Page not found.", ld=None)))

    # ---- robots, sitemap, llms.txt
    robots = ["User-agent: *", "Allow: /", "", "# AI search and answer engines are welcome",
              *[f"User-agent: {b}\nAllow: /\n" for b in ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "ClaudeBot", "Google-Extended", "Applebot-Extended", "Bingbot"]]]
    if SITE:
        robots.append(f"Sitemap: {SITE}/sitemap.xml")
        urls = ["/", "/work/"] + [p["url"] for p in projects]
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
        sm.append("</urlset>")
        (DIST / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    (DIST / "robots.txt").write_text("\n".join(robots) + "\n", encoding="utf-8")
    base = SITE or ""
    llms = [f"# {D.PERSON['name']}", "", f"> {D.PERSON['title']} based in {D.PERSON['location']}. "
            "25+ client websites delivered and 25+ Google Business Profiles optimized for businesses in Canada, the UK, the UAE, Saudi Arabia and Pakistan.", "",
            "## Services", *[f"- {s['name']}: {s['lead']}" for s in D.SERVICES], "",
            "## Projects", *[f"- [{p['name']}]({base}{p['url']}): {p['scope']} · {p['industry']} · {p['platform']} · live at {p['live']}" for p in projects], "",
            "## Contact", f"- Email: {D.PERSON['email']}", f"- Phone/WhatsApp: {D.PERSON['phone']}", f"- LinkedIn: {D.PERSON['linkedin']}", ""]
    (DIST / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    print(f"Built {2 + len(projects) + 1} pages into {DIST}" + ("" if SITE else "\nNOTE: SITE_URL is empty, so canonical tags and sitemap.xml were skipped."))


if __name__ == "__main__":
    build()
