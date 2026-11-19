# Hunzala Saeed portfolio

A fast, animated static website. You edit the content in Python and run one command to rebuild the site.

## Folders
- `src/data.py`: all text, projects, videos, FAQ and contact details. **Edit this file.**
- `src/templates/`: page layouts (home, work, case study, 404).
- `assets/`: CSS, JavaScript, images, videos, and the GSAP and Lenis libraries.
- `dist/`: the finished website. **Upload this folder.** Don't edit it by hand; the build overwrites it.

## Rebuild after any change
```
pip install jinja2 pillow
python src/build.py
```
To preview it locally, run `python -m http.server 8765 --directory dist` and open http://localhost:8765

## Before you publish (important)
1. **Domain:** in `src/data.py`, set `SITE_URL = "https://www.your-domain.com"`, then rebuild.
   Until you do, the build leaves out the canonical tags, Open Graph URLs, VideoObject schema and sitemap.xml.
2. **Contact form:** create a free access key at web3forms.com and put it in `WEB3FORMS_KEY`.
   Without a key, the form opens the visitor's email app with the message filled in.
3. Upload the contents of `dist/` to your hosting: Netlify, Cloudflare Pages, Vercel or cPanel `public_html`.
   On Vercel, `vercel.json` already handles caching and serves `dist/` (no build step needed on Vercel).
4. Add the site to Google Search Console and Bing Webmaster Tools, then submit `sitemap.xml`.
5. Put the portfolio link on your LinkedIn, and keep your name and title the same everywhere (this helps GEO).

## Adding website screenshots
Screenshots taken in a normal browser live in `assets/img/raw/` (19 sites, above-the-fold view). Prodigy Group's hero is a
background video that doesn't show in screenshots, so its preview is mostly blank. To replace any preview, take a full-page screenshot of the homepage at 1440 px wide (a browser extension such as
GoFullPage works). Save it as `assets/img/raw/<project-slug>.png`, for example `assets/img/raw/advance-therapy-uk.png`,
using the slug from `data.py`. Then rebuild. The build converts and crops it automatically.

## Adding Google Search Console results to a case study
Save the real screenshot in `assets/gsc/` and add this to the project in `data.py`:
```python
gsc=[{"src": "/assets/gsc/milton-tires-clicks.webp", "alt": "Search Console clicks for miltontires.ca", "caption": "Clicks, Jan–Jun 2026"}],
```
Use only real screenshots.

## Changing your About photo
Replace `assets/img/profile-original.png` (or use .jpg) with any portrait photo, ideally 4:5, then rebuild.
The build only resizes it to 900 px wide. It doesn't retouch the photo.

## Adding a video
Export the video at 540×960 (H.264, about 1–5 MB). Put `slug.mp4` and a `slug.jpg` poster in `assets/video/`, add a line to `VIDEOS` in `data.py`, then rebuild.

## What's included for SEO, AEO and GEO
- Unique titles and meta descriptions, one H1 per page, breadcrumbs, and alt text on images
- JSON-LD schema: Person, WebSite, ProfilePage, FAQPage, ItemList, CreativeWork, BreadcrumbList, and VideoObject (once SITE_URL is set)
- `robots.txt` that welcomes AI crawlers (GPTBot, PerplexityBot, ClaudeBot, Google-Extended…), plus `llms.txt`
- The FAQ is written as direct answers, and the hero is an "AI answer" block containing clear, citable facts
- All text is in the HTML, so crawlers can read it without JavaScript. Animations respect "reduce motion".
