# -*- coding: utf-8 -*-
"""All portfolio content in one place. Edit here, then run: python src/build.py

Rules used for this content:
- Only facts verified on the live sites (Nov 2026) or given by Hunzala.
- No invented results, rankings, traffic numbers or testimonials.
- To add real Search Console screenshots: put the image in assets/gsc/ and set "gsc" on the project.
"""

# Set this to the live domain before publishing, e.g. "https://www.yourdomain.com"
# (no trailing slash). Canonical tags, Open Graph URLs, VideoObject schema and
# sitemap.xml are only generated when it is set.
SITE_URL = ""

# Web3Forms access key for the contact form (free at web3forms.com).
# Empty = the form opens the visitor's email app with the message pre-filled.
WEB3FORMS_KEY = ""

PERSON = {
    "name": "Hunzala Saeed",
    "short": "HS",
    "title": "SEO, AEO & GEO Specialist, WordPress Developer & Video Editor",
    "location": "Rawalpindi, Pakistan",
    "locality": "Rawalpindi",
    "country": "PK",
    "email": "hunzalasaeed890@gmail.com",
    "phone": "+92 324 5217334",
    "phone_e164": "+923245217334",
    "whatsapp": "https://wa.me/923245217334",
    "linkedin": "https://www.linkedin.com/in/hunzalasaeed890",
}

STATS = [
    ("25", "+", "client websites delivered"),
    ("25", "+", "Google Business Profiles optimized"),
    ("4", "+", "years in SEO & web development"),
    ("5", "", "countries: Canada, UK, UAE, KSA, Pakistan"),
]

SERVICES = [
    {
        "id": "seo", "num": "01", "name": "SEO",
        "lead": "Technical, on-page and local SEO that makes a website easy to crawl, easy to understand and worth ranking.",
        "items": ["Website audits & indexing fixes", "Keyword & competitor research", "On-page optimization & internal linking",
                  "Schema markup", "Site speed & Core Web Vitals", "Backlink & citation building"],
        "tools": "Ahrefs · Semrush · Screaming Frog · Search Console · GA4",
    },
    {
        "id": "aeo-geo", "num": "02", "name": "AEO & GEO",
        "lead": "Answer Engine and Generative Engine Optimization, so your brand is the answer in Google AI Overviews, ChatGPT and Gemini.",
        "items": ["Question-led content structure", "FAQ content & FAQ schema", "Entity & brand consistency",
                  "AI crawler access (robots.txt)", "Citable facts on every page", "AI search visibility checks"],
        "tools": "Google AI Overviews · ChatGPT · Gemini · Perplexity",
    },
    {
        "id": "local-seo", "num": "03", "name": "Local SEO & Google Business Profile",
        "lead": "More calls, direction requests and walk-ins from people searching nearby. 25+ Google Business Profiles optimized so far.",
        "items": ["Google Business Profile optimization", "City & neighbourhood landing pages", "Local citations & NAP consistency",
                  "LocalBusiness schema", "Location-focused content", "Map pack visibility"],
        "tools": "Google Business Profile · Rank Math · Search Console",
    },
    {
        "id": "web-development", "num": "04", "name": "WordPress & Web Development",
        "lead": "Fast, responsive websites built to convert, mostly on WordPress and Elementor, plus Shopify and custom builds.",
        "items": ["WordPress & Elementor builds", "WooCommerce & Shopify stores", "Theme & plugin customization",
                  "HTML, CSS & JavaScript", "Speed, security & maintenance", "SEO-ready page structure"],
        "tools": "WordPress · Elementor · WooCommerce · LiteSpeed Cache · Wordfence",
    },
    {
        "id": "video-editing", "num": "05", "name": "Video Editing & Motion",
        "lead": "Scroll-stopping reels, YouTube videos, promo ads and motion graphics that make a brand look as good as it is.",
        "items": ["Reels, Shorts & TikTok", "YouTube video editing", "Promo & ad videos", "Motion graphics & animated text",
                  "Social media graphics", "Thumbnails & covers"],
        "tools": "Premiere Pro · After Effects · CapCut · Photoshop · Canva",
    },
]

SEO_DEV = "SEO + Development"
DEV = "Development"

PROJECTS = [
    # ---------------- SEO + Development ----------------
    dict(slug="milton-tires", name="Milton Tires", domain="miltontires.ca", industry="Tires & Auto Repair",
         location="Milton, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=True, accent="#E8442E",
         summary="A local tire shop in Milton that needed its website and search presence to bring in seasonal tire and brake customers.",
         services=["Tire sales & installation", "Tire storage", "Balancing & rotation", "Flat repair", "TPMS service", "Brake repair"],
         highlights=["Dedicated service pages for tire services and brake repair",
                     "BreadcrumbList, WebSite and WebPage schema on the live site",
                     "Seasonal winter tire and brake videos for social media"],
         videos=["milton-winter-tires", "milton-winter-brake"]),
    dict(slug="fort-erie-pit-stop", name="Fort Erie Pit Stop", domain="forteriepitstop.ca", industry="Auto Repair & Maintenance",
         location="Fort Erie, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=True, accent="#F2A33A",
         summary="An auto repair shop in Fort Erie with a clear service menu, published pricing and local search coverage across the Niagara area.",
         services=["Synthetic oil change", "Tire change & repair", "Brake service & repair", "3D wheel alignment",
                   "DriveON safety inspection", "Auto maintenance"],
         highlights=["A dedicated page for each of its 6 core services",
                     "Pricing, service areas and FAQ pages that answer buyer questions",
                     "FAQPage schema live on the site"],
         videos=[]),
    dict(slug="advance-therapy-canada", name="Advance Therapy Canada", domain="adtherapy.ca", industry="Autism & ABA Therapy",
         location="Mississauga, Ontario · serving Canada", scope=SEO_DEV, platform="WordPress", featured=True, accent="#3E8EDE",
         summary="An ABA therapy provider serving families across Canada, with service pages and city landing pages built for local search.",
         services=["ABA therapy at home", "ABA therapy at daycare", "Early intervention", "Children's assessments",
                   "Virtual autism therapy", "Parent coaching"],
         highlights=["27 city landing pages across Ontario, British Columbia, Alberta and Manitoba",
                     "MedicalBusiness, FAQPage and ItemList schema on the live site",
                     "Brand videos for social media"],
         videos=["advance-therapy-possibilities"]),
    dict(slug="advance-therapy-uk", name="Advance Therapy UK", domain="adtherapy.uk", industry="Autism & ABA Therapy",
         location="United Kingdom (UK-wide in-home service)", scope=SEO_DEV, platform="WordPress", featured=True, accent="#5B7CFA",
         summary="The UK site for in-home ABA therapy, written in UK English for UK families and built to rank for UK searches.",
         services=["In-home ABA therapy", "ABA therapy at daycare", "Early intervention", "Children's assessments",
                   "Virtual autism therapy", "Parent coaching"],
         highlights=["Content written in UK English for a UK audience",
                     "MedicalTherapy, FAQPage and AdministrativeArea schema on the live site",
                     "Seasonal winter video for UK social media"],
         videos=["advance-therapy-uk-winter"]),
    dict(slug="ontario-aba-therapy", name="Ontario ABA Therapy", domain="ontarioabatherapy.com", industry="Autism & ABA Therapy",
         location="Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=False, accent="#2BB39B",
         summary="An ABA therapy website for Ontario families, with a funding guide and service-area coverage across the province.",
         services=["Autism therapy services", "Ontario Autism Program (OAP) guidance", "In-home ABA", "Virtual autism care"],
         highlights=["21 Ontario service areas listed on the site",
                     "A dedicated Ontario Autism Program (OAP) funding page",
                     "MedicalBusiness, OfferCatalog and FAQPage schema on the live site"],
         videos=[]),
    dict(slug="smile-lounge-dentistry", name="Smile Lounge Dentistry", domain="smilelounge.ca", industry="Dental Clinic",
         location="Milton, Ontario, Canada", scope=SEO_DEV, platform="Next.js", featured=False, accent="#36B5C9",
         summary="A dental clinic in Milton with a modern website, local SEO and a steady stream of patient-friendly social videos.",
         services=["Our services", "About the clinic", "Patient blog", "Contact"],
         highlights=["Dentist schema with the clinic's full address",
                     "Services, about, blog and contact pages",
                     "Patient education reels, including insurance-benefit and nervous-patient videos"],
         videos=["smile-lounge-benefits", "smile-nervous-patients"]),
    dict(slug="bajwa-cpa", name="Bajwa CPA", domain="bajwacpa.com", industry="Accounting & Tax",
         location="Brampton & Mississauga, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=True, accent="#C9A227",
         summary="A CPA firm serving Brampton, Mississauga and the GTA, with a service page for every type of tax and accounting work.",
         services=["Corporate tax returns", "Personal tax returns", "Bookkeeping", "Non-resident tax returns",
                   "Incorporation & registration", "Tax planning"],
         highlights=["12 dedicated service pages, from corporate tax to business consulting",
                     "Tax checklists and filing-deadline resources",
                     "AccountingService, FAQPage, Article and Person schema on the live site"],
         videos=[]),
    dict(slug="autaq-banquet-hall", name="Autaq Banquet Hall", domain="autaqbanquethall.ca", industry="Banquet Hall & Events",
         location="Mississauga, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=False, accent="#B8860B",
         summary="A banquet hall in Mississauga for weddings and events, with service pages for catering, decor and event planning.",
         services=["Event services", "Catering services", "Stage decor", "Tent & outdoor events", "Event planning"],
         highlights=["EventVenue, LocalBusiness and FAQPage schema on the live site",
                     "Separate pages for each event service",
                     "Local SEO for Mississauga and GTA event searches"],
         videos=[]),
    dict(slug="aba-therapy-toronto", name="ABA Therapy Toronto", domain="abatherapytoronto.ca", industry="Autism & ABA Therapy",
         location="Toronto, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=False, accent="#E26D5A",
         summary="A Toronto ABA therapy website built around local SEO, clear service pages and family-friendly content.",
         services=["Clinic-based ABA", "At-home ABA", "ABA therapy at daycare"],
         highlights=["Tagline on the site: “Better Skills. Brighter Futures.”",
                     "MedicalBusiness, OfferCatalog and FAQPage schema on the live site",
                     "Dedicated daycare ABA service page for Toronto"],
         videos=[]),
    dict(slug="aba-therapy-mississauga", name="ABA Therapy Mississauga", domain="abatherapymississauga.ca", industry="Autism & ABA Therapy",
         location="Mississauga, Ontario, Canada", scope=SEO_DEV, platform="WordPress", featured=False, accent="#7A6FF0",
         summary="A Mississauga ABA therapy website targeting families neighbourhood by neighbourhood.",
         services=["In-home ABA", "Daycare ABA", "Virtual ABA", "Our approach"],
         highlights=["13 Mississauga neighbourhoods covered, from Meadowvale to Port Credit",
                     "MedicalBusiness, GeoCoordinates and FAQPage schema on the live site",
                     "Service, approach and blog pages"],
         videos=[]),
    dict(slug="advance-academy", name="Advance Academy", domain="advanceacademy.ca", industry="Autism Services & Education",
         location="Mississauga, Ontario · serving Canada", scope=SEO_DEV, platform="WordPress", featured=True, accent="#1F9D8B",
         summary="Autism ABA therapy and education across Canada, with city pages and training content.",
         services=["ABA therapy", "Autism education", "City-based services across Canada"],
         highlights=["City pages for 13 cities, from Toronto to Vancouver and Calgary",
                     "LocalBusiness, FAQPage and OpeningHoursSpecification schema on the live site",
                     "ABA training promo video"],
         videos=["advance-academy-training"]),
    dict(slug="the-herb-house", name="The Herb House", domain="herbhouse.ca", industry="Natural Health Retail",
         location="Pickering & Scarborough, Ontario · ships across Canada", scope=SEO_DEV, platform="Shopify", featured=True, accent="#5FA34A",
         summary="A natural health store with two Ontario locations and an online shop that ships across Canada.",
         services=["Vitamins & supplements", "Herbal products", "Sports nutrition", "Immune, cold & flu",
                   "Stress, anxiety & sleep", "Hair, skin & nails"],
         highlights=["Shopify store with Canada-wide shipping",
                     "Product collections organized by health need",
                     "BreadcrumbList schema on the live site"],
         videos=[]),
    # ---------------- Development ----------------
    dict(slug="advance-therapy-global", name="Advance Therapy (Global)", domain="adtherapy.net", industry="Autism & ABA Therapy",
         location="Canada, USA, India, UAE & UK", scope=DEV, platform="WordPress", featured=False, accent="#4C8DF6",
         summary="The global Advance Therapy website, presenting autism services for families in five countries.",
         services=["ABA therapy", "Diagnostic evaluations", "Expressive & receptive language", "Behaviour reduction",
                   "Academic readiness", "Caregiver ABA coaching"], highlights=[], videos=[]),
    dict(slug="ash-beauty-salon", name="Ash Beauty Salon", domain="ashbeautysalon.ca", industry="Beauty Salon & Laser",
         location="Mississauga, Ontario, Canada", scope=DEV, platform="Custom build", featured=False, accent="#C98B7B",
         summary="A hair, nails, skin and laser salon in Mississauga with an elegant, fast custom-coded website.",
         services=["Laser hair removal", "Nails", "Hair", "Facials & skin", "Waxing"], highlights=[],
         videos=["ash-punjabi-motion", "ash-treatment-room"]),
    dict(slug="metacode", name="Metacode", domain="metacode.sa", industry="Immersive Technology",
         location="Saudi Arabia", scope=DEV, platform="Next.js", featured=True, accent="#7C5CFF",
         summary="An immersive technology company building VR, AR, AI and digital twin solutions.",
         services=["Geographic information systems", "Immersive solutions", "AI virtual visits", "Agentic AI solutions",
                   "VR gamification", "Digital twins"], highlights=[], videos=[]),
    dict(slug="prodigy-group", name="Prodigy Group", domain="prodigygroup.ae", industry="Business Setup Services",
         location="Business Bay, Dubai, UAE", scope=DEV, platform="WordPress", featured=False, accent="#D4AF37",
         summary="A Dubai business setup firm covering company formation, licensing, visas and accounting.",
         services=["Company formation", "Business licensing", "Visa & Golden Visa", "Business centre", "Tax & VAT",
                   "Accounting & bookkeeping"], highlights=[], videos=[]),
    dict(slug="king-tire", name="King Tire Trading", domain="kingtire.ca", industry="Tire Retail",
         location="Toronto, Ontario, Canada", scope=DEV, platform="Custom build", featured=False, accent="#E0B341",
         summary="A Toronto tire retailer offering quality tires, competitive pricing and expert installation.",
         services=["Tire sales", "Tire installation", "Tire balancing", "Maintenance & vehicle care"], highlights=[], videos=[]),
    dict(slug="on-the-ball", name="On the Ball", domain="ontheball.co", industry="Sales & Leadership Training",
         location="", scope=DEV, platform="Custom build", featured=False, accent="#F06A3F",
         summary="A sales development and leadership training company helping teams build better performance.",
         services=["Sales training", "Leadership training", "Enterprise training", "Membership", "Marketing services"],
         highlights=[], videos=[]),
    dict(slug="le-banquet", name="Le Banquet", domain="lebanquethalls.ca", industry="Banquet Hall & Events",
         location="Concord, Vaughan, Ontario, Canada", scope=DEV, platform="WordPress", featured=False, accent="#C2A36B",
         summary="An elegant banquet hall in Concord, Vaughan for weddings, corporate and social events.",
         services=["Wedding venue", "Corporate events", "Social events", "Birthday parties"], highlights=[], videos=[]),
    dict(slug="ayu-foundation", name="AYU Foundation", domain="ayufoundation.com", industry="Nonprofit · Autism Support",
         location="Canada", scope=DEV, platform="WordPress", featured=False, accent="#F2994A",
         summary="A nonprofit initiative supporting autistic children and their families across Canada.",
         services=["Family support & guidance", "Community programs", "Education & awareness", "Direct assistance"],
         highlights=[], videos=[]),
    dict(slug="tng-sunrise-services", name="TNG Sunrise Services", domain="tngsunriseservices.com", industry="Financial Services",
         location="Brampton, Ontario, Canada", scope=DEV, platform="WordPress", featured=False, accent="#F5A524",
         summary="A Brampton financial services firm covering accounting, tax, credit, loans and mortgages.",
         services=["Accounting & tax", "Financial planning", "Credit repair", "Consumer proposal support",
                   "Loan consulting", "Mortgages & refinancing"], highlights=[], videos=[]),
    dict(slug="j-fiber-max", name="J Fiber Max", domain="jfibermax.com", industry="Fiber Internet Provider",
         location="Rawalpindi, Pakistan", scope=DEV, platform="WordPress", featured=False, accent="#1E88E5",
         summary="A fiber internet provider in Rawalpindi offering home and business packages, IPTV and dedicated bandwidth.",
         services=["Fiber internet for homes & businesses", "IPTV", "Dedicated bandwidth", "Internet packages",
                   "Free installation"], highlights=[], videos=[]),
    dict(slug="eskaynet-it-services", name="Eskaynet IT Services", domain="eskaynet.ca", industry="IT Services",
         location="Brampton, Ontario, Canada", scope=DEV, platform="WordPress", featured=False, accent="#00A6A6",
         summary="A Brampton IT services company providing managed support, networking and cloud solutions.",
         services=["IT support & helpdesk", "Systems administration", "Network infrastructure", "Cloud & virtualization",
                   "Business continuity", "IT consulting"], highlights=[], videos=[]),
    dict(slug="creative-gurus", name="Creative Gurus", domain="creativegurus.ca", industry="Creative & Digital Agency",
         location="", scope=DEV, platform="Next.js", featured=False, accent="#D4FF3A",
         summary="A creative and digital growth agency website for strategy, web, SEO, social media and content.",
         services=["Strategy & branding", "Website design & development", "SEO & organic growth", "Social media marketing",
                   "Paid advertising", "Creative content"], highlights=[], videos=[]),
]

VIDEOS = [
    dict(slug="furniture-commercial", title="Showroom Commercial", brand="Karachi Furniture Showroom", kind="Commercial"),
    dict(slug="korso-ai-painter", title="Paint Can Holster Product Ad", brand="KORSO", kind="Product ad"),
    dict(slug="milton-winter-brake", title="Winter Brake Check", brand="Milton Tires", kind="Reel"),
    dict(slug="ash-punjabi-motion", title="Punjabi Motion Reel", brand="Ash Beauty Salon", kind="Motion reel"),
    dict(slug="advance-therapy-possibilities", title="A World of Possibilities", brand="Advance Therapy", kind="Motion graphics"),
    dict(slug="smile-nervous-patients", title="For Nervous Patients", brand="Smile Lounge Dentistry", kind="Reel"),
    dict(slug="furniture-step-inside", title="Step Inside", brand="Karachi Furniture Showroom", kind="Commercial"),
    dict(slug="advance-therapy-uk-winter", title="Winter Support at Home", brand="Advance Therapy UK", kind="Motion graphics"),
    dict(slug="milton-winter-tires", title="Winter Tires", brand="Milton Tires", kind="Reel"),
    dict(slug="ash-treatment-room", title="In the Treatment Room", brand="Ash Beauty Salon", kind="Reel"),
    dict(slug="smile-lounge-benefits", title="Use Your Dental Benefits", brand="Smile Lounge Dentistry", kind="Reel"),
    dict(slug="furniture-wood-to-home", title="From Wood to Home", brand="Karachi Furniture Showroom", kind="Brand story"),
    dict(slug="advance-academy-training", title="ABA Training Promo", brand="Advance Academy", kind="Promo"),
]

EXPERIENCE = [
    dict(role="Technical Manager", focus="SEO, AEO, GEO, WordPress & Video", company="Creative Gurus",
         where="Rawalpindi, Pakistan", dates="Jun 2024 – Sep 2026",
         text="Led SEO and website delivery for client brands: technical, on-page and local SEO, AEO and GEO, WordPress builds, Google Business Profiles and video editing."),
    dict(role="SEO Executive", focus="AEO, GEO & Local SEO", company="Decodex Technology",
         where="Rawalpindi, Pakistan", dates="Jul 2023 – Mar 2024",
         text="Keyword research, competitor analysis, on-page and local SEO campaigns, Google Business Profile optimization and structured content for AI platforms."),
    dict(role="WordPress Developer & SEO Specialist", focus="", company="Virtual Netz",
         where="Rahim Yar Khan, Pakistan", dates="Sep 2021 – Mar 2023",
         text="Built and maintained WordPress and WooCommerce websites, customized themes and plugins, and implemented on-page SEO."),
]

EDUCATION = [
    dict(title="BS Mathematics · GPA 3.64 / 4.00", org="Khawaja Fareed University of Engineering & IT (KFUEIT)", dates="2020 – 2024"),
    dict(title="Local SEO Course", org="Skills Heaven", dates=""),
]

PROCESS = [
    ("Audit", "Crawl the site, read Search Console and GA4, and study the competitors already ranking."),
    ("Plan", "Map keywords and questions to pages, plan internal links, schema and content."),
    ("Build", "Develop or fix the website: fast, mobile-first, clean structure, ready to rank."),
    ("Answer", "Structure content as clear answers so Google AI Overviews, ChatGPT and Gemini can cite it."),
    ("Grow", "Optimize the Google Business Profile, publish content and video, and report progress."),
]

FAQ = [
    ("What is the difference between SEO, AEO and GEO?",
     "SEO (Search Engine Optimization) helps your website rank in Google's regular results. AEO (Answer Engine Optimization) "
     "structures your content as clear answers so it can appear in featured answers and voice search. GEO (Generative Engine "
     "Optimization) helps AI tools like ChatGPT, Gemini and Google AI Overviews understand, trust and cite your brand. "
     "I work on all three together, because they rely on the same foundation: a fast, well-structured site with clear, factual content."),
    ("Do you work with clients outside Pakistan?",
     "Yes. Most of my projects are for businesses in Canada, and I have also worked on websites for clients in the United Kingdom, "
     "the United Arab Emirates and Saudi Arabia. I work remotely and adjust to your time zone for calls."),
    ("Which platforms do you build websites on?",
     "Mostly WordPress with Elementor, including WooCommerce stores. I have also worked on Shopify, Next.js and custom-coded websites."),
    ("Can you optimize my Google Business Profile?",
     "Yes. I have optimized more than 25 Google Business Profiles, covering categories, services, descriptions, photos, "
     "location pages on the website and local citations."),
    ("How do you report SEO progress?",
     "With data from Google Search Console and Google Analytics 4: impressions, clicks, rankings for target keywords, "
     "indexed pages and the leads your website brings in."),
    ("Do you also edit videos for social media?",
     "Yes. I edit reels, YouTube Shorts, TikTok and YouTube videos, promo ads and motion graphics using Adobe Premiere Pro, "
     "After Effects and CapCut, and design graphics in Photoshop and Canva."),
]
