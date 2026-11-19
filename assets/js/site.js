/* Hunzala Saeed portfolio: motion + interactions. Content works without this file. */
(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;
  const hasGsap = typeof window.gsap !== 'undefined';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const store = { get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
                  set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} } };

  /* ---------- mobile menu ---------- */
  const menuBtn = $('.menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = root.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', open);
    });
    $$('.mnav a').forEach(a => a.addEventListener('click', () => { root.classList.remove('menu-open'); menuBtn.setAttribute('aria-expanded', false); }));
  }

  /* ---------- video lightbox + hover play (works without GSAP) ---------- */
  const lb = $('.lightbox');
  const lbVideo = lb && $('video', lb);
  const openLb = (src, poster, cap) => {
    if (!lb) return;
    lbVideo.src = src; lbVideo.poster = poster || '';
    $('.lightbox__cap', lb).textContent = cap || '';
    lb.classList.add('is-open'); lb.setAttribute('aria-hidden', 'false');
    lbVideo.play().catch(() => {});
    $('.lightbox__close', lb).focus();
  };
  const closeLb = () => { if (!lb) return; lbVideo.pause(); lbVideo.removeAttribute('src'); lbVideo.load(); lb.classList.remove('is-open'); lb.setAttribute('aria-hidden', 'true'); };
  if (lb) {
    $('.lightbox__close', lb).addEventListener('click', closeLb);
    lb.addEventListener('click', e => { if (e.target === lb) closeLb(); });
    addEventListener('keydown', e => { if (e.key === 'Escape') closeLb(); });
  }
  $$('.vcard').forEach(card => {
    const v = $('video', card);
    const src = card.dataset.src;
    $('.cover', card).addEventListener('click', () => openLb(src, card.dataset.poster, card.dataset.cap));
    if (!fine || reduce || !v) return;
    card.addEventListener('mouseenter', () => {
      if (!v.src) { v.src = src; }
      v.currentTime = 0; v.play().then(() => card.classList.add('is-playing')).catch(() => {});
    });
    card.addEventListener('mouseleave', () => { v.pause(); card.classList.remove('is-playing'); });
  });

  /* hero showreel: play only when visible */
  const reel = $('.phone video');
  if (reel && !reduce) {
    const io = new IntersectionObserver(([e]) => { e.isIntersecting ? reel.play().catch(() => {}) : reel.pause(); });
    io.observe(reel);
  } else if (reel) { reel.removeAttribute('autoplay'); reel.pause(); }

  /* ---------- project filters ---------- */
  $$('.filter').forEach(btn => btn.addEventListener('click', () => {
    const f = btn.dataset.filter;
    $$('.filter').forEach(b => b.setAttribute('aria-pressed', b === btn));
    $$('.grid .pcard').forEach(c => c.classList.toggle('is-out', f !== 'all' && c.dataset.scope !== f));
    if (window.ScrollTrigger) ScrollTrigger.refresh();
  }));

  /* card spotlight + scroll height var */
  $$('.pcard').forEach(c => {
    c.addEventListener('pointermove', e => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--mx', `${e.clientX - r.left}px`); c.style.setProperty('--my', `${e.clientY - r.top}px`);
    });
    const view = $('.browser__view', c);
    if (view) { const set = () => c.style.setProperty('--vh', view.clientHeight + 'px'); set(); addEventListener('resize', set); }
  });

  /* ---------- contact form ---------- */
  const form = $('#contact-form');
  if (form) form.addEventListener('submit', async e => {
    e.preventDefault();
    const msg = $('.form__msg', form);
    const d = Object.fromEntries(new FormData(form));
    if (d.botcheck) return;
    const key = form.dataset.key;
    if (!key) {
      const body = `Name: ${d.name}\nEmail: ${d.email}\nService: ${d.service}\n\n${d.message}`;
      location.href = `mailto:${form.dataset.mail}?subject=${encodeURIComponent('Project enquiry from ' + d.name)}&body=${encodeURIComponent(body)}`;
      msg.textContent = 'Opening your email app…';
      return;
    }
    msg.textContent = 'Sending…';
    try {
      const r = await fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ access_key: key, subject: 'New portfolio enquiry', ...d }) });
      const j = await r.json();
      msg.textContent = j.success ? 'Thank you! I will reply within one business day.' : 'Something went wrong. Please email me directly.';
      if (j.success) form.reset();
    } catch (err) { msg.textContent = 'Network error. Please email me directly.'; }
  });

  /* ---------- year ---------- */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  if (!hasGsap || reduce) { root.classList.add('no-loader'); $$('[data-reveal]').forEach(el => { el.style.opacity = 1; el.style.transform = 'none'; }); return; }

  /* =================== MOTION =================== */
  gsap.registerPlugin(ScrollTrigger);

  /* keep the GSAP ticker awake: some browsers/webviews pause it after tab or viewport changes */
  let lastTick = performance.now();
  gsap.ticker.add(() => { lastTick = performance.now(); });
  const nudge = () => { if (performance.now() - lastTick > 250) gsap.ticker.wake(); };
  ['scroll', 'pointerdown', 'touchstart', 'pageshow', 'focus'].forEach(ev => addEventListener(ev, nudge, { passive: true }));
  document.addEventListener('visibilitychange', nudge);
  setInterval(nudge, 700);

  /* smooth scroll */
  let lenis = null;
  if (window.Lenis && fine) {
    lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const t = $(a.getAttribute('href')); if (!t) return; e.preventDefault(); lenis.scrollTo(t, { offset: -80 });
    }));
  }

  /* header hide on scroll down */
  const hdr = $('.hdr'); let lastY = 0;
  ScrollTrigger.create({ start: 0, end: 'max', onUpdate: self => {
    const y = self.scroll();
    hdr.classList.toggle('is-solid', y > 40);
    hdr.classList.toggle('is-hidden', y > 300 && y > lastY && !root.classList.contains('menu-open'));
    lastY = y;
  }});

  /* cursor + glow */
  if (fine) {
    root.classList.add('has-cursor');
    const dot = $('.cursor'), ring = $('.cursor-ring'), glow = $('.glow');
    const xd = gsap.quickTo(dot, 'x', { duration: .12 }), yd = gsap.quickTo(dot, 'y', { duration: .12 });
    const xr = gsap.quickTo(ring, 'x', { duration: .45, ease: 'power3' }), yr = gsap.quickTo(ring, 'y', { duration: .45, ease: 'power3' });
    const xg = glow && gsap.quickTo(glow, 'x', { duration: 2.2, ease: 'power2' }), yg = glow && gsap.quickTo(glow, 'y', { duration: 2.2, ease: 'power2' });
    addEventListener('pointermove', e => { xd(e.clientX); yd(e.clientY); xr(e.clientX); yr(e.clientY); if (xg) { xg(e.clientX); yg(e.clientY); } });
    const label = $('span', ring);
    $$('a,button,summary,[data-cursor]').forEach(el => {
      el.addEventListener('mouseenter', () => {
        const l = el.closest('[data-cursor]')?.dataset.cursor;
        if (l) { ring.classList.add('is-label'); label.textContent = l; } else ring.classList.add('is-link');
      });
      el.addEventListener('mouseleave', () => ring.classList.remove('is-link', 'is-label'));
    });
    /* magnetic */
    $$('[data-magnetic]').forEach(el => {
      const xm = gsap.quickTo(el, 'x', { duration: .6, ease: 'elastic.out(1,.4)' }), ym = gsap.quickTo(el, 'y', { duration: .6, ease: 'elastic.out(1,.4)' });
      el.addEventListener('pointermove', e => { const r = el.getBoundingClientRect(); xm((e.clientX - r.left - r.width / 2) * .35); ym((e.clientY - r.top - r.height / 2) * .35); });
      el.addEventListener('pointerleave', () => { xm(0); ym(0); });
    });
  }

  /* split headings into masked lines of words */
  $$('[data-split]').forEach(el => {
    const html = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = html.map(line => `<span class="split-line"><span>${line}</span></span>`).join('');
  });
  const splitIn = (el, delay = 0) => gsap.from($$('.split-line > span', el), { yPercent: 110, rotate: 2, duration: 1.1, ease: 'power4.out', stagger: .09, delay });

  /* ---------- intro ---------- */
  const loader = $('.loader');
  const heroIntro = () => {
    const hero = $('.hero');
    if (!hero) { $$('.page-intro [data-split]').forEach(el => splitIn(el, .1)); return; }
    const tl = gsap.timeline({ defaults: { ease: 'power4.out' } });
    const q = $('.hero__query .q'); const full = q ? q.textContent : '';
    if (q) q.textContent = '';
    tl.from('.hero__query', { y: 20, opacity: 0, duration: .8 })
      .add(() => { if (!q) return; let i = 0; const t = setInterval(() => { q.textContent = full.slice(0, ++i); if (i >= full.length) clearInterval(t); }, 28); }, '-=.4');
    $$('.hero__display .split-line > span').length && tl.from('.hero__display .split-line > span', { yPercent: 110, duration: 1.1, stagger: .1 }, .2);
    tl.from('.answer', { y: 40, opacity: 0, duration: 1 }, .9)
      .from('.answer .w', { opacity: .08, duration: .05, stagger: .018, ease: 'none' }, 1.2)
      .from('.answer .chip', { y: 12, opacity: 0, stagger: .06, duration: .5 }, '-=.6')
      .from('.hero__cta > *', { y: 20, opacity: 0, stagger: .08, duration: .7 }, '-=.4')
      .from('.phone', { y: 80, rotate: 6, opacity: 0, duration: 1.4 }, .5)
      .from('.float-tag', { scale: .6, opacity: 0, stagger: .15, duration: .8, ease: 'back.out(2)' }, 1.3);
    // failsafe: never leave hero content hidden
    setTimeout(() => { if (tl.progress() < 1) { tl.progress(1); if (q) q.textContent = full; } }, 4500);
  };
  // wrap answer words for the "AI is writing" reveal (text stays in the DOM for crawlers)
  $$('.answer p').forEach(p => {
    const walk = node => [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(w => { if (!w) return; if (/^\s+$/.test(w)) frag.append(w); else { const s = document.createElement('span'); s.className = 'w'; s.textContent = w; frag.append(s); } });
        n.replaceWith(frag);
      } else if (n.nodeType === 1) walk(n);
    });
    walk(p);
  });

  if (loader && !store.get('seen')) {
    store.set('seen', 1);
    const num = $('.loader__num', loader); const o = { v: 0 };
    gsap.timeline()
      .to(o, { v: 100, duration: 1, ease: 'power2.inOut', onUpdate: () => num.textContent = Math.round(o.v) })
      .to(loader, { yPercent: -100, duration: .9, ease: 'power4.inOut' })
      .add(heroIntro, '-=.5')
      .set(loader, { display: 'none' });
  } else { if (loader) loader.style.display = 'none'; heroIntro(); }

  /* ---------- scroll reveals ---------- */
  $$('[data-split]').forEach(el => {
    if (el.closest('.hero') || el.closest('.page-intro')) return;
    gsap.from($$('.split-line > span', el), { yPercent: 110, rotate: 2, duration: 1.1, ease: 'power4.out', stagger: .09,
      scrollTrigger: { trigger: el, start: 'top 88%' } });
  });
  $$('[data-reveal]').forEach(el => gsap.to(el, { opacity: 1, y: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%' } }));
  ScrollTrigger.batch('[data-stagger] > *', { start: 'top 92%', onEnter: els => gsap.from(els, { y: 50, opacity: 0, stagger: .08, duration: .9, ease: 'power3.out', overwrite: true }) });

  /* counters */
  $$('[data-count]').forEach(el => {
    const end = +el.dataset.count; const o = { v: 0 };
    gsap.to(o, { v: end, duration: 2, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 95%' }, onUpdate: () => el.firstChild.nodeValue = Math.round(o.v) });
  });

  /* marquee speeds up + flips with scroll velocity */
  const track = $('.marquee__track');
  if (track) {
    const anims = track.getAnimations ? track.getAnimations() : [];
    ScrollTrigger.create({ onUpdate: s => { const v = s.getVelocity(); anims.forEach(a => a.playbackRate = gsap.utils.clamp(-6, 6, (v / 400) || 1) || 1); } });
    addEventListener('scrollend', () => anims.forEach(a => a.playbackRate = 1));
  }

  /* services: stacked cards shrink as the next one arrives */
  const svcs = $$('.svc');
  if (innerWidth > 860) svcs.forEach((card, i) => {
    if (i === svcs.length - 1) return;
    gsap.to(card, { scale: .94 - (svcs.length - i) * .006, opacity: .55, ease: 'none',
      scrollTrigger: { trigger: svcs[i + 1], start: 'top bottom', end: 'top 20%', scrub: true } });
  });

  /* horizontal featured work */
  const pin = $('.hwork__pin'), htrack = $('.hwork__track');
  if (pin && htrack) {
    ScrollTrigger.matchMedia({ '(min-width: 901px)': () => {
      const dist = () => htrack.scrollWidth - innerWidth + 40;
      const tw = gsap.to(htrack, { x: () => -dist(), ease: 'none',
        scrollTrigger: { trigger: pin, start: 'top top', end: () => '+=' + dist(), pin: true, scrub: 1, invalidateOnRefresh: true, anticipatePin: 1 } });
      $$('.pcard', htrack).forEach(card => gsap.from($('.browser', card), { yPercent: 12, rotate: -2, ease: 'none',
        scrollTrigger: { trigger: card, containerAnimation: tw, start: 'left right', end: 'center center', scrub: true } }));
      const bar = $('.hwork__progress i');
      if (bar) gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: pin, start: 'top top', end: () => '+=' + dist(), scrub: true } });
    }});
  }

  /* video wall parallax columns */
  $$('.vwall .vcard').forEach((c, i) => {
    if (innerWidth < 700) return;
    gsap.to(c, { y: (i % 2 ? -50 : 30), ease: 'none', scrollTrigger: { trigger: c, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* process line draw */
  const fill = $('.process__fill');
  if (fill) {
    const vertical = innerWidth <= 900;
    gsap.to(fill, { [vertical ? 'scaleY' : 'scaleX']: 1, ease: 'none',
      scrollTrigger: { trigger: '.process', start: 'top 75%', end: 'bottom 55%', scrub: true,
        onUpdate: s => $$('.step').forEach((st, i, a) => st.classList.toggle('is-on', s.progress >= i / a.length)) } });
  }

  /* case-study screenshot scroll */
  const csImg = $('.cs-shot .browser__view img');
  if (csImg && csImg.offsetHeight - csImg.parentElement.offsetHeight > 80) gsap.to(csImg, { y: () => -(csImg.offsetHeight - csImg.parentElement.offsetHeight), ease: 'none',
    scrollTrigger: { trigger: '.cs-shot', start: 'top 20%', end: '+=1400', scrub: 1, pin: innerWidth > 900 ? '.cs-shot' : false, invalidateOnRefresh: true } });

  /* about portrait: clip reveal, zoom-out, parallax, 3D tilt */
  const portrait = $('.portrait');
  if (portrait) {
    const frame = $('.portrait__frame', portrait), img = $('img, .portrait__ph', frame);
    gsap.timeline({ scrollTrigger: { trigger: portrait, start: 'top 80%' } })
      .fromTo(frame, { clipPath: 'inset(100% 0% 0% 0% round 36px)' }, { clipPath: 'inset(0% 0% 0% 0% round 36px)', duration: 1.4, ease: 'power4.inOut' })
      .from(img, { scale: 1.35, duration: 1.8, ease: 'power3.out' }, 0)
      .from('.portrait__back', { x: -22, y: -22, opacity: 0, duration: 1.2, ease: 'power3.out' }, .5)
      .from('.portrait__badge', { scale: 0, rotate: -180, duration: 1.1, ease: 'back.out(1.6)' }, .7)
      .from('.portrait__chip', { y: 30, opacity: 0, scale: .8, stagger: .15, duration: .8, ease: 'back.out(2)' }, .9);
    if (img && img.tagName === 'IMG') gsap.to(img, { yPercent: -8, ease: 'none', scrollTrigger: { trigger: portrait, start: 'top bottom', end: 'bottom top', scrub: true } });
    gsap.to('.portrait__back', { x: 34, y: 34, ease: 'none', scrollTrigger: { trigger: portrait, start: 'top bottom', end: 'bottom top', scrub: true } });
    if (fine) {
      const rx = gsap.quickTo(frame, 'rotationX', { duration: .6, ease: 'power3' }), ry = gsap.quickTo(frame, 'rotationY', { duration: .6, ease: 'power3' });
      portrait.addEventListener('pointermove', e => {
        const r = portrait.getBoundingClientRect(), px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
        ry((px - .5) * 14); rx((.5 - py) * 14);
        frame.style.setProperty('--sx', px * 100 + '%'); frame.style.setProperty('--sy', py * 100 + '%');
      });
      portrait.addEventListener('pointerleave', () => { rx(0); ry(0); });
    }
  }

  /* footer giant name */
  const big = $('.ftr__big');
  if (big) gsap.from(big, { yPercent: 40, opacity: .2, ease: 'none', scrollTrigger: { trigger: big, start: 'top bottom', end: 'bottom bottom', scrub: true } });

  addEventListener('load', () => ScrollTrigger.refresh());
})();
