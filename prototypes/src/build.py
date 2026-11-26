import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data import *
D = os.path.dirname(__file__)
css = {k: open(f'{D}/css_{k}.css').read() for k in ('a2','b2','c2')}

def head(title, fonts, style):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<link rel="stylesheet" href="{fonts}">
<style>{style}</style>
</head>
<body>
'''

# ---------- shared partials ----------
LOGO_CSS = '''
/* Partner logos: monochrome strip, company colors on hover */
.logos{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:26px 40px;margin:30px auto 0;max-width:940px}
.lg{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:var(--lg-ink);font-family:var(--lg-font);font-size:13px;letter-spacing:.1em;text-transform:uppercase;transition:color .25s}
.lg img{height:34px;width:auto;display:block;filter:grayscale(1) contrast(1.05);opacity:.72;mix-blend-mode:multiply;transition:filter .3s,opacity .3s}
.lg.tile img{height:30px;border-radius:6px}
.lg.white img{height:24px;filter:brightness(0);opacity:.62}
.lg.bluedot img{height:22px}
.lg.sentient img{height:40px}
.lg:hover{color:var(--lg-hover)}
.lg:hover img{filter:none;opacity:1}
.lg.white:hover img{filter:brightness(0);opacity:.9}
.guest{margin-top:8px}
.guest a{color:var(--lg-hover)}
html,body{overflow-x:clip}
'''

def logos_html():
    out = []
    for f, label, href, kind in LOGOS:
        cls = 'lg ' + kind + (' ' + f if f in ('bluedot','sentient') else '')
        alt = label or {'miri':'MIRI','far':'FAR.AI','bluedot':'BlueDot Impact','sentient':'Sentient Futures'}[f]
        out.append(f'<a class="{cls}" href="{href}"><img src="img/logo/{f}.png" alt="{alt}">' + (f'<span>{label}</span>' if label else '') + '</a>')
    return '<div class="logos">' + ''.join(out) + '</div>'

def events_li(fmt):
    return ''.join(fmt(d, t, n) for d, t, n in EVENTS)

FOOT_COPY = 'A project of Manifund · <a href="#">Donate</a>'
QUESTIONS = 'Questions? Contact <a href="#">robin@moxsf.com</a>'

# =====================================================================
# A2 · The Building
# =====================================================================
a_css = css['a2'] + LOGO_CSS + '''
:root{--lg-ink:var(--ink-2);--lg-hover:var(--rust);--lg-font:var(--mono)}
.who-list{display:grid;grid-template-columns:1fr 1fr;font-size:14.5px;text-align:center}
.who-list span{padding:7px 4px;border-bottom:1px solid #EEEEEC}
.who-list span:nth-child(odd){border-right:1px solid #EEEEEC}
.photos{grid-template-columns:repeat(3,1fr)}
.photos figure{aspect-ratio:4/3}
.staff{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:22px;text-align:left}
.sc{display:grid;grid-template-columns:112px 1fr;gap:18px;background:var(--card);border:1px solid var(--rule);padding:16px;min-width:0}
.sc img{width:112px;height:112px;object-fit:cover;filter:grayscale(.15)}
.sc .role{font-family:var(--mono);font-size:11px;letter-spacing:.12em;color:var(--ink-2)}
.sc h4{font-family:var(--text);font-weight:400;font-size:17px;margin:4px 0 8px;line-height:1.35}
.sc h4 b{font-weight:700}
.sc h4 i{color:var(--rust)}
.tags{display:flex;flex-wrap:wrap;gap:5px;align-items:center;font-family:var(--mono);font-size:11px}
.tags .k{color:var(--ink-2);margin-right:2px}
.tags span:not(.k){border:1px solid var(--rule);padding:2px 7px;color:var(--ink)}
.sc .mail{display:block;margin-top:8px;font-family:var(--mono);font-size:12px;color:var(--rust)}
.grp{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin:40px 0 0;text-align:left;border-bottom:1px solid var(--ink);padding-bottom:8px;display:flex;justify-content:space-between}
.mem{display:grid;grid-template-columns:repeat(2,1fr);gap:0 28px;text-align:left}
.m{display:grid;grid-template-columns:52px 1fr;gap:14px;align-items:center;padding:11px 0;border-bottom:1px solid var(--rule);min-width:0}
.m img{width:52px;height:52px;border-radius:50%;object-fit:cover}
.m p{margin:0;font-size:15px;line-height:1.35}
.m b{font-weight:700}
.m i{color:var(--rust)}
.m small{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2)}
@media (max-width:760px){.staff,.mem{grid-template-columns:1fr}.sc{grid-template-columns:84px 1fr}.sc img{width:84px;height:84px}}
footer a{color:inherit}
.arrs{display:flex;flex-direction:column;gap:3px;padding-right:12px;border-right:1px solid #A9ACAF}
.arr{all:unset;cursor:pointer;display:grid;place-items:center;width:18px;height:13px;border-radius:2px}
.arr svg{width:10px;height:8px;fill:#45484B;transition:fill .3s,filter .3s}
.arr:hover svg{fill:#1E1B18}
.arr.lit svg{fill:var(--signal);filter:drop-shadow(0 0 4px rgba(235,88,9,.8))}
.arr:focus-visible{outline:2px solid var(--signal);outline-offset:2px}
@media (max-width:480px){.elevator{gap:11px;padding:8px 12px}.elevator .lbl{min-width:0}}
'''

def a_build():
    staff = ''.join(f'''<article class="sc"><img src="img/people/{s}.jpg" alt="{n}"><div><span class="role">{r}</span><h4><b>{n}</b> {into(a,b)}</h4><div class="tags"><span class="k">contact for:</span>{''.join(f'<span>{t}</span>' for t in tags)}</div><span class="mail">{mail}</span></div></article>''' for s, r, n, a, b, tags, mail in STAFF)
    mem = ''.join(f'<div class="m"><img src="img/people/{s}.jpg" alt="{n}"><p><small>{g}</small><b>{n}</b> {into(a,b)}</p></div>' for s, n, a, b, g in MEMBERS)
    gallery = ''.join(f'<figure><img src="img/site-{f}.jpg" alt="{alt}"></figure>' for f, alt in GALLERY)
    ev = events_li(lambda d, t, n: f'<li><span class="d"><b>{d}</b>{t.upper()}</span>{n}</li>')
    who = ''.join(f'<span>{g}</span>' for g in GATHER)
    rows, last = [], None
    for name, room in OFFICES:
        fl = room.split()[1][0]
        if fl != last:
            rows.append(f'<div class="row fl"><span>— {fl}00s —</span><span></span></div>'); last = fl
        rows.append(f'<div class="row"><span>{name}</span><span>{room.replace("Rooms ","").replace("Room ","")}</span></div>')
    return head('Mox · A2 · The Building', 'https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:wght@400;500&display=swap', a_css) + f'''
<div class="col top"><a class="l" href="#partners">Partner Orgs</a><a class="l" href="#space">The Space</a><a class="l" href="#humans">Mox Humans</a><a class="btn solid" href="#" style="padding:8px 14px">Login</a></div>
<div class="stage">
  <div class="bg" aria-hidden="true">
    <div class="lines"></div>
    <span class="win" style="left:57.2%;top:38.6%;width:5.9%;height:6%"></span>
    <span class="win" style="left:66%;top:48.2%;width:5.9%;height:6%;animation-delay:-6s"></span>
    <span class="win" style="left:57.2%;top:58.2%;width:5.9%;height:6%;animation-delay:-11s"></span>
    <div class="fade"></div>
  </div>
  <header class="hero"><div class="col in">
    <a class="lockup" href="#" aria-label="Mox"><span class="mark" aria-hidden="true"></span><span class="word">Mox</span></a>
    <p class="tag">{TAGLINE}</p>
    <a class="addr" href="#"><span class="dot" aria-hidden="true"></span>{ADDRESS}</a>
  </div></header>
  <div class="col"><div class="three">
    <article class="card"><div class="ph"><img src="img/site-014.jpg" alt="A talk in the lounge"></div><div class="b"><h3>Upcoming events</h3><ul class="ev body">{ev}</ul><div class="foot"><a href="#">All events →</a></div></div></article>
    <article class="card"><div class="ph"><img src="img/site-023.jpg" alt="A speaker presenting a chart" style="animation-delay:-9s"></div><div class="b"><h3>Who we gather</h3><div class="who-list body">{who}</div><div class="foot"><a href="#humans">See people →</a></div></div></article>
    <article class="card"><div class="ph"><img src="img/site-003.jpg" alt="A meeting room with a city view" style="animation-delay:-16s"></div><div class="b"><h3>Space for meaningful work</h3><div class="ways body"><a class="btn solid" href="#">Apply for membership</a><a class="btn line" href="#">Inquire about offices</a><a class="btn line" href="#">Buy a day pass</a></div><div class="foot"><a href="#">Member portal →</a></div></div></article>
  </div></div>
</div>
<main class="col">
  <section id="partners" data-floor="1" data-name="Partner Orgs">
    <span class="floor"><b>1</b>Partner Orgs</span>
    <p class="sub guest">Learn more about our <a href="#">guest program</a></p>
    {logos_html()}
  </section>
  <section id="space" data-floor="2" data-name="The Space">
    <span class="floor"><b>2</b>The Space</span>
    <div class="photos">{gallery}</div>
  </section>
  <section id="humans" data-floor="3" data-name="Mox Humans">
    <span class="floor"><b>3</b>Mox Humans</span>
    <div class="counts"><div><b>215</b><span>MEMBERS</span></div></div>
    <div class="grp"><span>Staff</span></div>
    <div class="staff">{staff}</div>
    <div class="grp"><span>Members</span><a href="#" style="color:var(--rust);text-decoration:none">See people →</a></div>
    <div class="mem">{mem}</div>
  </section>
  <section id="offices" data-floor="4" data-name="Offices">
    <span class="floor"><b>4</b>Offices</span>
    <div class="board" role="table" aria-label="Offices"><h4>1680 · OFFICES</h4>{''.join(rows)}</div>
  </section>
  <section class="close" style="padding-block:70px 40px">
    <div class="ctas"><a class="btn solid" href="#">Apply for membership</a><a class="btn line" href="#">Inquire about offices</a><a class="btn line" href="#">Buy a day pass</a></div>
    <p class="sub" style="margin-top:22px">{QUESTIONS}</p>
  </section>
</main>
<footer>{FOOT_COPY}</footer>
<nav class="elevator" aria-label="Sections">
  <span class="arrs"><button class="arr" id="aup" type="button" aria-label="Up one floor"><svg viewBox="0 0 10 8" aria-hidden="true"><path d="M5 0 10 8H0z"/></svg></button><button class="arr" id="adn" type="button" aria-label="Down one floor"><svg viewBox="0 0 10 8" aria-hidden="true"><path d="M5 8 0 0h10z"/></svg></button></span>
  <a href="#partners" data-f="1">1</a><a href="#space" data-f="2">2</a><a href="#humans" data-f="3">3</a><a href="#offices" data-f="4">4</a>
  <span class="lbl" id="flbl">Lobby</span>
</nav>
<script>
(function(){{
  var links=[].slice.call(document.querySelectorAll('.elevator a')),lbl=document.getElementById('flbl'),secs=[].slice.call(document.querySelectorAll('section[data-floor]'));
  function upd(){{var mid=scrollY+innerHeight*.5,f=0,n='Lobby';secs.forEach(function(s){{if(s.offsetTop<=mid){{f=+s.dataset.floor;n=s.dataset.name}}}});cur=f;links.forEach(function(a){{a.classList.toggle('on',+a.dataset.f===f)}});lbl.textContent=n}}
  var up=document.getElementById('aup'),dn=document.getElementById('adn'),lastY=scrollY,cur=0,t;
  function floorTop(f){{return f<=0?0:secs[f-1].getBoundingClientRect().top+scrollY-24}}
  function go(f){{f=Math.max(0,Math.min(secs.length,f));scrollTo({{top:floorTop(f),behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}})}}
  up.onclick=function(){{go(cur+1)}};dn.onclick=function(){{go(cur-1)}};
  function dir(){{var y=scrollY;if(Math.abs(y-lastY)>2){{up.classList.toggle('lit',y>lastY);dn.classList.toggle('lit',y<lastY);clearTimeout(t);t=setTimeout(function(){{up.classList.remove('lit');dn.classList.remove('lit')}},500)}}lastY=y}}
  addEventListener('scroll',function(){{upd();dir()}},{{passive:true}});upd();
}})();
</script>
</body></html>'''

# =====================================================================
# B2 · Control Panel
# =====================================================================
b_css = css['b2'] + LOGO_CSS + '''
:root{--lg-ink:var(--ink-2);--lg-hover:var(--signal);--lg-font:var(--mono)}
.board .r{grid-template-columns:2.4em 2.6em 1fr;white-space:normal}
.board .r span:last-child{white-space:normal;line-height:1.3;padding-block:3px}
.board{font-size:14px}
.logos-panel{margin:28px auto 0;background:var(--panel);border-radius:14px;padding:26px 24px;box-shadow:inset 0 1px 0 #fff,0 1px 0 #B9BBBD}
.logos-panel .logos{margin-top:0}
.staff{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:26px;text-align:left}
.badge{background:linear-gradient(180deg,#F1F1EF,#E2E3E3);border-radius:14px;padding:12px;box-shadow:inset 0 1px 0 #fff,inset 0 -2px 0 #B9BBBD,0 20px 30px -24px rgba(0,0,0,.5);display:flex;flex-direction:column;gap:10px;min-width:0}
.badge .bz{background:#1B1C1D;border-radius:8px;padding:6px}
.badge img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:3px;filter:saturate(.85)}
.badge .role{font-family:var(--mono);font-size:10px;letter-spacing:.12em;color:var(--signal)}
.badge h4{margin:0;font-family:var(--serif);font-weight:400;font-size:24px;line-height:1.05}
.badge p{margin:0;font-size:13.5px;color:var(--ink-2)}
.badge p i{font-style:normal;color:var(--ink)}
.badge .tags{display:flex;flex-wrap:wrap;gap:5px;font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.04em}
.badge .tags span{background:var(--panel);border-radius:4px;padding:3px 6px;box-shadow:0 2px 0 #A9ABAE}
.badge .tags .k{background:none;box-shadow:none;padding:3px 0;color:var(--ink-2)}
.badge .mail{font-family:var(--mono);font-size:11.5px;color:var(--ink)}
.mgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:16px;text-align:left}
.mb{display:grid;grid-template-columns:48px 1fr;gap:10px;align-items:center;background:var(--panel);border-radius:10px;padding:8px;box-shadow:inset 0 1px 0 #fff,0 1px 0 #B9BBBD;min-width:0}
.mb img{width:48px;height:48px;border-radius:6px;object-fit:cover;box-shadow:0 0 0 3px #1B1C1D}
.mb p{margin:0;font-size:12.5px;line-height:1.3;color:var(--ink-2)}
.mb b{display:block;color:var(--ink);font-weight:500;font-size:13.5px}
.mb small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--signal)}
.sub-h{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--ink-2);text-transform:uppercase;margin-top:40px;display:flex;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:8px}
@media (max-width:900px){.staff{grid-template-columns:1fr 1fr}.mgrid{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.mgrid{grid-template-columns:1fr}.staff{gap:10px}.badge{padding:9px}.badge h4{font-size:19px}.badge .tags{font-size:9px}}
footer a,.foot2 a{color:inherit}
'''

def b_build():
    staff = ''.join(f'''<article class="badge"><div class="bz"><img src="img/people/{s}.jpg" alt="{n}"></div><span class="role">{r}</span><h4>{n}</h4>{f'<p>{into(a,b)}</p>' if a else ''}<div class="tags"><span class="k">contact for:</span>{''.join(f'<span>{t}</span>' for t in tags)}</div><span class="mail">{mail}</span></article>''' for s, r, n, a, b, tags, mail in STAFF)
    mem = ''.join(f'<div class="mb"><img src="img/people/{s}.jpg" alt="{n}"><p><small>{g}</small><b>{n}</b>{into(a,b)}</p></div>' for s, n, a, b, g in MEMBERS)
    sheet = ''.join(f'<figure><img src="img/site-{f}.jpg" alt="{alt}"><figcaption><span>{i+1:02d}A</span><span></span></figcaption></figure>' for i, (f, alt) in enumerate(GALLERY))
    ev = ''.join(f'<div class="r"><span>{d}</span><span>{t.upper()}</span><span>{n}</span></div>' for d, t, n in EVENTS)
    caps = ''.join(f'<span class="cap">{g}</span>' for g in GATHER)
    return head('Mox · B2 · Control Panel', 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400;500&family=Doto:wght@700;900&display=swap', b_css) + f'''
<div class="col top">
  <span><span class="led" aria-hidden="true"></span>{ADDRESS.upper()}</span>
  <nav><a href="#partners">Partner Orgs</a><a href="#space">The Space</a><a href="#humans">Mox Humans</a><a class="key dark" href="#"><span class="sh"></span><span class="ed"></span><span class="fc" style="min-height:34px;padding:8px 14px;font-size:11px">Login</span></a></nav>
</div>
<div class="stage">
  <div class="bp" aria-hidden="true"><div class="lines"></div><div class="fade"></div></div>
  <header class="col hero">
    <a class="lockup" href="#" aria-label="Mox"><span class="mark" aria-hidden="true"></span><span class="word">Mox</span></a>
    <p class="tag">{TAGLINE.replace('<em>','<i>').replace('</em>','</i>')}</p>
    <div class="ctas">
      <a class="key orange" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Apply for membership</span></a>
      <a class="key" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Buy a day pass</span></a>
    </div>
  </header>
  <div class="col three">
    <article class="pnl"><div class="hd"><span class="screw"></span><span class="lab">01</span><span class="screw"></span></div>
      <div class="bezel"><div class="win"><img src="img/site-014.jpg" alt="A talk in the lounge"></div></div>
      <h3>Upcoming events</h3><div class="board" id="board">{ev}</div>
      <div class="ft"><a class="key dark block" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">All events →</span></a></div></article>
    <article class="pnl"><div class="hd"><span class="screw"></span><span class="lab">02</span><span class="screw"></span></div>
      <div class="bezel"><div class="win"><img src="img/site-023.jpg" alt="A speaker presenting a chart"></div></div>
      <h3>Who we gather</h3><div class="caps">{caps}</div>
      <div class="ft"><a class="lnk" href="#humans">See people →</a></div></article>
    <article class="pnl"><div class="hd"><span class="screw"></span><span class="lab">03</span><span class="screw"></span></div>
      <div class="bezel"><div class="win"><img src="img/site-003.jpg" alt="A meeting room with a city view"></div></div>
      <h3>Space for meaningful work</h3>
      <div class="stack">
        <a class="key orange block" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Apply for membership</span></a>
        <a class="key block" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Inquire about offices</span></a>
        <a class="key block" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Buy a day pass</span></a>
      </div>
      <div class="ft"><a class="lnk" href="#">Member portal →</a></div></article>
  </div>
</div>
<main class="col">
  <section id="partners">
    <span class="idx">PARTNER ORGS</span>
    <p class="sub guest">Learn more about our <a href="#">guest program</a></p>
    <div class="logos-panel">{logos_html()}</div>
  </section>
  <section id="space">
    <span class="idx">THE SPACE</span>
    <div class="sheet">{sheet}</div>
  </section>
  <section id="humans">
    <span class="idx">MOX HUMANS</span>
    <p class="sub">215 members</p>
    <div class="sub-h"><span>Staff</span></div>
    <div class="staff">{staff}</div>
    <div class="sub-h"><span>Members</span><a href="#" style="text-decoration:none;color:var(--ink)">See people →</a></div>
    <div class="mgrid">{mem}</div>
  </section>
  <div class="final">
    <div class="ctas" style="margin-top:0"><a class="key orange" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Apply for membership</span></a><a class="key" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Inquire about offices</span></a><a class="key" href="#"><span class="sh"></span><span class="ed"></span><span class="fc">Buy a day pass</span></a></div>
    <p class="foot2" style="margin-top:22px">{QUESTIONS}</p>
  </div>
</main>
<footer>{FOOT_COPY}</footer>
<script>
(function(){{
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var rows=document.getElementById('board').children,fi=0;
  setInterval(function(){{var r=rows[fi%rows.length];r.classList.remove('flip');void r.offsetWidth;r.classList.add('flip');fi++}},2600);
}})();
</script>
</body></html>'''

# =====================================================================
# C2 · The Commons
# =====================================================================
c_css = css['c2'] + LOGO_CSS + '''
:root{--lg-ink:var(--ink-2);--lg-hover:var(--forest);--lg-font:var(--sans)}
.lg{font-weight:600;font-size:12px}
.now{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap}
.now img{width:40px;height:40px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 2px var(--mint)}
.now .sw{display:inline-flex;align-items:center;gap:12px}
.who-pills{display:grid;grid-template-columns:1fr 1fr;gap:7px;align-content:start}
.who-pills span{text-align:center;line-height:1.3;font-size:13px;padding:7px 8px;border:1px solid #B8CBB9;border-radius:999px;color:var(--forest);background:#F4F8F4}
.ways{display:flex;flex-direction:column;gap:9px}
.ways .btn{justify-content:center}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:26px 22px;margin-top:36px}
.gal figure{margin:0;background:#fff;padding:9px 9px 11px;box-shadow:0 20px 36px -24px rgba(0,0,0,.55),0 0 0 1px #ECECEC;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.gal figure:nth-child(3n+1){transform:rotate(-1.6deg)}
.gal figure:nth-child(3n+2){transform:rotate(1.1deg)}
.gal figure:nth-child(3n){transform:rotate(-.5deg)}
.gal figure:hover{transform:rotate(0) scale(1.03)}
.gal img{aspect-ratio:4/3;object-fit:cover;width:100%}
@media (max-width:620px){.gal{grid-template-columns:1fr 1fr;gap:14px}}
.staff{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:30px;text-align:left}
.sc{background:#fff;border-radius:14px;padding:12px 12px 16px;box-shadow:0 22px 36px -28px rgba(0,0,0,.5),0 0 0 1px var(--rule);display:flex;flex-direction:column;gap:8px;min-width:0;transition:transform .3s}
.sc:hover{transform:translateY(-4px)}
.sc .ph{position:relative;transform:rotate(-1deg);transition:transform .4s}
.sc:hover .ph{transform:rotate(0)}
.sc img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:4px}
.sc .role{font-size:11px;font-weight:600;letter-spacing:.08em;color:var(--green);margin-top:4px}
.sc h4{margin:0;font-family:var(--serif);font-weight:400;font-size:24px;line-height:1.1}
.sc p{margin:0;font-family:var(--serif);font-size:16px;color:var(--ink-2);line-height:1.3}
.sc .tags{display:flex;flex-wrap:wrap;gap:5px;font-size:11.5px}
.sc .tags span{border:1px solid #B8CBB9;border-radius:999px;padding:2px 8px;color:var(--forest);background:#F4F8F4}
.sc .tags .k{border:0;background:none;padding:2px 0;color:var(--ink-2)}
.sc .mail{font-size:13px;font-weight:600;color:var(--rust)}
@media (max-width:900px){.staff{grid-template-columns:1fr 1fr}}
.mlist{max-width:860px;margin:18px auto 0;display:grid;grid-template-columns:1fr 1fr;gap:0 32px;text-align:left}
.hm{display:grid;grid-template-columns:52px 1fr;gap:14px;align-items:center;padding:11px 0;border-bottom:1px solid var(--rule)}
.hm img{width:52px;height:52px;border-radius:50%;object-fit:cover}
.hm p{margin:0;font-family:var(--serif);font-size:17px;line-height:1.3}
.hm i{color:var(--ink-2)}
.hm small{display:block;font-family:var(--sans);font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--green);margin-bottom:2px}
@media (max-width:700px){.mlist{grid-template-columns:1fr}}
.grp{font-size:12.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);margin-top:44px}
footer.ft2{background:var(--forest);color:#C9D6CA;text-align:center;font-size:14px;padding-block:40px}
footer.ft2 a{color:#fff}
'''

def c_build():
    staff = ''.join(f'''<article class="sc"><div class="ph"><img src="img/people/{s}.jpg" alt="{n}"></div><span class="role">{r}</span><h4>{n}</h4>{f'<p>{into(a,b)}</p>' if a else ''}<div class="tags"><span class="k">contact for:</span>{''.join(f'<span>{t}</span>' for t in tags)}</div><span class="mail">{mail}</span></article>''' for s, r, n, a, b, tags, mail in STAFF)
    mem = ''.join(f'<div class="hm"><img src="img/people/{s}.jpg" alt="{n}"><p><small>{g}</small>{n} <i>{into(a,b).replace("<i>","").replace("</i>","")}</i></p></div>' for s, n, a, b, g in MEMBERS)
    gal = ''.join(f'<figure><img src="img/site-{f}.jpg" alt="{alt}"></figure>' for f, alt in GALLERY)
    ev = events_li(lambda d, t, n: f'<li><span class="d">{d} {t.upper()}</span>{n}</li>')
    who = ''.join(f'<span>{g}</span>' for g in GATHER)
    rot = [[s, n, a, b] for s, n, a, b, g in MEMBERS[:8]]
    import json
    return head('Mox · C2 · The Commons', 'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Public+Sans:wght@400;500;600&display=swap', c_css) + f'''
<div class="stage">
  <div class="sk" aria-hidden="true"><div class="lines"></div></div>
  <div class="col top"><a class="l" href="#partners">Partner Orgs</a><a class="l" href="#space">The Space</a><a class="l" href="#humans">Mox Humans</a><a class="btn primary" href="#" style="padding:8px 16px;font-size:13.5px">Login</a></div>
  <header class="col hero">
    <a class="lockup" href="#" aria-label="Mox"><span class="mark" aria-hidden="true"></span><span class="word">Mox</span></a>
    <p class="tag">{TAGLINE}</p>
    <p class="now" id="now" aria-live="polite"><span class="sw"><img id="n-img" src="img/people/{rot[0][0]}.jpg" alt=""><span><b id="n0">{rot[0][1]}</b> is into <i id="n1">{rot[0][2]}</i> and <i id="n2">{rot[0][3]}</i></span></span></p>
    <div class="ctas"><a class="btn primary" href="#">Apply for membership</a><a class="btn ghost" href="#">Buy a day pass</a></div>
  </header>
</div>
<div class="col three">
  <article class="card"><div class="print"><span class="tape" aria-hidden="true"></span><img src="img/site-014.jpg" alt="A talk in the lounge"></div>
    <div class="b"><h3>Upcoming events</h3><ul class="ev body">{ev}</ul><div class="ft"><a href="#">All events →</a></div></div></article>
  <article class="card"><div class="print"><span class="tape" aria-hidden="true"></span><img src="img/site-023.jpg" alt="A speaker presenting a chart"></div>
    <div class="b"><h3>Who we gather</h3><div class="who-pills body">{who}</div><div class="ft"><a href="#humans">See people →</a></div></div></article>
  <article class="card"><div class="print"><span class="tape" aria-hidden="true"></span><img src="img/site-003.jpg" alt="A meeting room with a city view"></div>
    <div class="b"><h3>Space for meaningful work</h3><div class="ways body"><a class="btn green" href="#">Apply for membership</a><a class="btn out" href="#">Inquire about offices</a><a class="btn out" href="#">Buy a day pass</a></div><div class="ft"><a href="#">Member portal →</a></div></div></article>
</div>
<main class="col">
  <section id="partners">
    <div class="kick">Partner Orgs</div>
    <p class="sub guest">Learn more about our <a href="#">guest program</a></p>
    {logos_html()}
  </section>
  <section id="space">
    <h2>The Space</h2>
    <div class="gal">{gal}</div>
  </section>
  <section id="humans">
    <h2>Mox Humans</h2>
    <div class="stats"><div><b>215</b>members</div></div>
    <div class="grp">Staff</div>
    <div class="staff">{staff}</div>
    <div class="grp">Members</div>
    <div class="mlist">{mem}</div>
    <a class="btn out" href="#" style="margin-top:26px">See people →</a>
  </section>
  <section style="padding-bottom:84px">
    <div class="ctas"><a class="btn green" href="#">Apply for membership</a><a class="btn out" href="#">Inquire about offices</a><a class="btn out" href="#">Buy a day pass</a></div>
  </section>
</main>
<footer class="ft2"><div>{FOOT_COPY}</div><div style="margin-top:6px">{QUESTIONS}</div></footer>
<script>
(function(){{
  var ppl={json.dumps(rot)};
  var el=document.getElementById('now'),i=0;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  setInterval(function(){{el.classList.add('out');setTimeout(function(){{i=(i+1)%ppl.length;var p=ppl[i];document.getElementById('n-img').src='img/people/'+p[0]+'.jpg';for(var k=0;k<3;k++)document.getElementById('n'+k).innerHTML=p[k+1];el.classList.remove('out')}},550)}},4600);
}})();
</script>
</body></html>'''


# =====================================================================
# D2 · The Building, in full: the drawing first, content arrives on scroll
# =====================================================================
D_CSS = """
/* D2: the first screen is only the lockup, the tagline and the whole building. Content rises in as you scroll. */
.bg{position:fixed;left:50%;top:var(--bt,240px);width:var(--bw,600px);transform:translateX(-50%);z-index:0;transition:opacity .2s linear}
.bg .lines{opacity:.42}
.bg{opacity:var(--bo,1)}
.stage{overflow:visible;padding:0}
.hero{min-height:100vh;min-height:100svh;padding-block:18px 0;display:flex;flex-direction:column}
.hero .in{z-index:1}
.cue{margin-top:auto;padding-bottom:18px;display:flex;flex-direction:column;align-items:center;gap:6px;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-2);text-decoration:none;position:relative;z-index:1;transition:opacity .3s}
.cue i{display:block;width:1px;height:26px;background:var(--ink-2);transform-origin:top;animation:cue 2.8s ease-in-out infinite}
@keyframes cue{0%{transform:scaleY(0)}50%{transform:scaleY(1)}100%{transform:scaleY(1);opacity:0}}
.after{position:relative;z-index:1}
.three{margin-top:0}
.top{position:relative;z-index:2}
main,footer{position:relative;z-index:1}
footer{background:var(--paper)}
.board{position:relative}
.js .rv{opacity:0;transform:translateY(28px);transition:opacity .9s ease,transform .9s cubic-bezier(.2,.7,.2,1)}
.js .rv.in{opacity:1;transform:none}
.elevator{opacity:0;pointer-events:none;transition:opacity .4s}
.elevator.show{opacity:1;pointer-events:auto}
@media (prefers-reduced-motion:reduce){.js .rv{opacity:1;transform:none;transition:none}.cue i{animation:none;transform:none}.bg{transition:none}}
"""

def d_build():
    h = a_build().replace('Mox · A2 · The Building', 'Mox · D2 · The Building, in full')
    h = h.replace('</style>', D_CSS + '</style>', 1)
    h = h.replace('<html lang="en">', '<html lang="en"><script>document.documentElement.className="js"</script>', 1) if False else h.replace('<head>', '<head><script>document.documentElement.className="js"</script>', 1)
    h = h.replace('<div class="fade"></div>', '')
    # close the hero after the address with a scroll cue, then put the three cards below it
    h = h.replace('</div></header>\n  <div class="col"><div class="three">',
                  '</div><a class="cue" href="#enter" id="cue">Scroll to enter<i></i></a></header>\n  <div class="col after" id="enter"><div class="three">', 1)
    # reveal targets
    h = h.replace('<article class="card">', '<article class="card rv">')
    for tag in ('<span class="floor">', '<p class="sub guest">', '<div class="logos">', '<div class="photos">', '<div class="counts">', '<div class="staff">', '<div class="mem">', '<div class="board"', '<div class="ctas">'):
        h = h.replace(tag, tag.replace('class="', 'class="rv ', 1))
    h = h.replace('<div class="grp">', '<div class="grp rv">')
    js = """
<script>
(function(){
  var root=document.documentElement,bg=document.querySelector('.bg'),txt=document.querySelector('.hero .in'),cue=document.getElementById('cue'),el=document.querySelector('.elevator');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hero=document.querySelector('.hero');
  function layout(){
    if(scrollY<5) hero.style.minHeight=(innerHeight-hero.getBoundingClientRect().top)+'px';
    var top=txt.getBoundingClientRect().bottom+(scrollY>0?0:0)+18, room=innerHeight-top-(cue.offsetHeight+14);
    if(scrollY>0) top=parseFloat(root.style.getPropertyValue('--bt'))||top;
    var w=Math.min(innerWidth*0.96,1100,room*690/600);
    var t=top+Math.max(0,(room-w*600/690)/2);
    root.style.setProperty('--bw',w+'px');root.style.setProperty('--bt',t+'px');
  }
  function onScroll(){
    var p=Math.min(1,scrollY/(innerHeight*.8));
    root.style.setProperty('--bo',(1-.76*p).toFixed(3));
    cue.style.opacity=1-Math.min(1,p*3);
    el.classList.toggle('show',p>.6);
  }
  layout();onScroll();
  addEventListener('resize',function(){if(scrollY<5)layout()});
  addEventListener('scroll',onScroll,{passive:true});
  var items=[].slice.call(document.querySelectorAll('.rv'));
  if(reduce||!('IntersectionObserver' in window)){items.forEach(function(e){e.classList.add('in')});return}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var d=0;if(e.target.classList.contains('card'))d=[].indexOf.call(e.target.parentNode.children,e.target)*140;e.target.style.transitionDelay=d+'ms';e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -12% 0px'});
  items.forEach(function(e){io.observe(e)});
})();
</script>
</body></html>"""
    h = h.replace('if(s.offsetTop<=mid)', 'if(s.getBoundingClientRect().top+scrollY<=mid)')
    h = h.replace('</body></html>', js, 1)
    return h

# =====================================================================
# E2 · D2 plus B2's departure board and pushable keys; one join panel up front
# =====================================================================
E_CSS = """
/* E2: who we gather + space for meaningful work merged into one join console; events below on B2's departure board. */
:root{--chassis:#E0E1E2;--panel:#F4F4F2;--screen:#0E0F0F;--amber:#FF8A2B;--signal-2:#B94204;--dots:"Doto","IBM Plex Mono",monospace}
.key{--face:var(--panel);--edge:#A9ABAE;--txt:var(--ink);position:relative;display:block;border:0;padding:0;background:transparent;cursor:pointer;text-decoration:none;font:inherit;outline-offset:6px}
.key .sh{position:absolute;inset:0;border-radius:9px;background:rgba(0,0,0,.22);transform:translateY(4px);filter:blur(4px);transition:transform .25s cubic-bezier(.3,.7,.4,1)}
.key .ed{position:absolute;inset:0;border-radius:9px;background:var(--edge)}
.key .fc{position:relative;display:flex;align-items:center;justify-content:space-between;gap:14px;padding:16px 20px;border-radius:9px;background:var(--face);color:var(--txt);transform:translateY(-6px);transition:transform .25s cubic-bezier(.3,.7,.4,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.45);text-align:left}
.key:hover .fc{transform:translateY(-8px)}
.key:hover .sh{transform:translateY(6px)}
.key:active .fc{transform:translateY(-1px);transition-duration:34ms}
.key:active .sh{transform:translateY(1px)}
.key.orange{--face:var(--signal);--edge:var(--signal-2);--txt:#fff}
.key.rust{--face:var(--rust);--edge:#4A1F03;--txt:#fff}
.key.dark{--face:#2A2B2C;--edge:#0C0C0C;--txt:#F4F4F2}
.key .t{font-family:var(--mono);font-size:13.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:500}
.key .ar{font-family:var(--mono);font-size:18px;line-height:1}
.key.big .fc{padding:24px 24px}
.key.big .t{font-size:15px}
.key.sm .fc{padding:11px 16px}
.key.sm .t{font-size:11.5px}
.console{position:relative;background:linear-gradient(180deg,#E9EAEA,#DCDDDE);border-radius:18px;padding:30px;display:grid;grid-template-columns:1.05fr 1fr;gap:30px;text-align:left;
  box-shadow:inset 0 1px 0 #fff,inset 0 -2px 0 #B3B5B8,0 40px 60px -40px rgba(30,27,24,.55),0 1px 0 #C4C6C8}
.console .screw{position:absolute;width:9px;height:9px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#9C9EA0);box-shadow:inset 0 0 0 1px #8D8F92}
.console .screw:nth-of-type(1){left:12px;top:12px}.console .screw:nth-of-type(2){right:12px;top:12px}.console .screw:nth-of-type(3){left:12px;bottom:12px}.console .screw:nth-of-type(4){right:12px;bottom:12px}
.console h3{font-size:28px;margin:0 0 16px;text-align:center}
.bz{background:#1B1C1D;border-radius:10px;padding:7px;box-shadow:inset 0 0 0 1px #000}
.bz img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:4px}
.caps{display:grid;grid-template-columns:1fr 1fr;gap:10px 9px;margin-top:16px}
.cap{background:var(--panel);border-radius:7px;padding:10px 8px 9px;text-align:center;font-size:15px;color:var(--ink);box-shadow:0 3px 0 #A9ABAE,inset 0 1px 0 #fff;transition:transform .12s,box-shadow .12s;user-select:none}
.cap:hover{transform:translateY(2px);box-shadow:0 1px 0 #A9ABAE,inset 0 1px 0 #fff}
.side{display:flex;flex-direction:column;gap:14px;border-left:1px solid #C4C6C8;padding-left:30px}
.side .bz img{aspect-ratio:16/8}
.keys{display:flex;flex-direction:column;gap:16px;margin-top:6px}
.keys .pair{display:grid;grid-template-columns:1fr;gap:16px}
.side .foot{margin-top:auto;padding-top:14px;border-top:1px solid #C4C6C8;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;display:flex;justify-content:space-between;align-items:center;gap:12px}
.side .foot a{color:var(--rust);text-decoration:none}
.side .foot a:hover{text-decoration:underline}
.evs{margin-top:34px;background:linear-gradient(180deg,#E9EAEA,#DCDDDE);border-radius:18px;padding:26px 30px 30px;text-align:left;position:relative;
  box-shadow:inset 0 1px 0 #fff,inset 0 -2px 0 #B3B5B8,0 40px 60px -40px rgba(30,27,24,.55),0 1px 0 #C4C6C8;display:grid;grid-template-columns:270px 1fr;gap:26px;align-items:stretch}
.evs h3{font-size:28px;margin:0 0 14px}
.evs .l{display:flex;flex-direction:column}
.evs .l .bz{flex:1}
.evs .l .bz img{height:100%;aspect-ratio:auto;min-height:160px}
.board{border:7px solid #1B1C1D;background:var(--screen);border-radius:8px;padding:14px 18px;font-family:var(--dots);font-weight:700;font-size:19px;line-height:1.9;color:var(--amber);text-shadow:0 0 6px rgba(255,138,43,.6);text-transform:uppercase;box-shadow:inset 0 0 0 1px #000;position:relative;overflow:hidden}
.board::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.03) 0 1px,transparent 1px 3px);pointer-events:none}
.board .hd{display:grid;grid-template-columns:3em 3.4em 1fr;gap:12px;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.14em;color:#8C6A4D;text-shadow:none;border-bottom:1px solid #2A2B2C;padding-bottom:4px;margin-bottom:4px}
.board .r{display:grid;grid-template-columns:3em 3.4em 1fr;gap:12px;border-bottom:1px dashed #1F2020}
.board .r:last-child{border-bottom:0}
.board .r.flip span:last-child{animation:flip .5s steps(3)}
@keyframes flip{0%{opacity:.1}50%{opacity:.6}100%{opacity:1}}
.evs .ft{margin-top:16px;display:flex;justify-content:flex-end}
.evs .ft .key{display:inline-block}
@media (max-width:860px){.console{grid-template-columns:1fr;padding:24px 18px 26px}.side{border-left:0;padding-left:0;border-top:1px solid #C4C6C8;padding-top:22px}.evs{grid-template-columns:1fr;padding:22px 18px 24px}.evs .l .bz{flex:none}.evs .l .bz img{aspect-ratio:16/9;height:auto;min-height:0}.side .bz{display:none}}
@media (max-width:480px){.board{font-size:15px;padding:10px 12px}.board .r,.board .hd{grid-template-columns:2.6em 3em 1fr;gap:8px}.cap{font-size:14px}}
"""

def key(cls, label, href='#'):
    return f'<a class="key {cls}" href="{href}"><span class="sh"></span><span class="ed"></span><span class="fc"><span class="t">{label}</span><span class="ar" aria-hidden="true">→</span></span></a>'

def e_build():
    h = d_build().replace('Mox · D2 · The Building, in full', 'Mox · E2 · Building first, join up front')
    h = h.replace('</style>', E_CSS + '</style>', 1)
    h = h.replace('<head>', '<head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Doto:wght@700&display=swap">', 1)
    i = h.index('<div class="three">'); j = h.index('</div>\n</div>\n<main', i)
    caps = ''.join(f'<span class="cap">{g}</span>' for g in GATHER)
    rows = ''.join(f'<div class="r"><span>{d}</span><span>{t.upper()}</span><span>{n}</span></div>' for d, t, n in EVENTS)
    block = f"""<div class="console rv">
      <span class="screw"></span><span class="screw"></span><span class="screw"></span><span class="screw"></span>
      <div class="gather"><h3>Who we gather</h3><div class="bz"><img src="img/site-021.jpg" alt="Members making letters with their bodies in front of the green wall"></div><div class="caps">{caps}</div></div>
      <div class="side"><h3>Space for meaningful work</h3><div class="bz"><img src="img/site-003.jpg" alt="A meeting room with a city view"></div>
        <div class="keys">{key('orange big','Apply for membership')}{key('rust','Buy a day pass')}{key('sm','Inquire about offices')}</div>
        <div class="foot"><a href="#humans">See people →</a><a href="#">Member portal →</a></div></div>
    </div>
    <div class="evs rv"><span class="screw" style="position:absolute;left:12px;top:12px"></span>
      <div class="l"><h3>Upcoming events</h3><div class="bz"><img src="img/site-014.jpg" alt="A talk in the lounge"></div></div>
      <div><div class="board" id="board" role="table" aria-label="Upcoming events"><div class="hd"><span>DAY</span><span>TIME</span><span>EVENT</span></div>{rows}</div>
      <div class="ft">{key('dark sm','All events')}</div></div>
    </div>"""
    h = h[:i] + block + h[j:]
    flick = """<script>(function(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;var rows=document.querySelectorAll('#board .r'),i=0;setInterval(function(){var r=rows[i%rows.length];r.classList.remove('flip');void r.offsetWidth;r.classList.add('flip');i++},2600)})();</script>
</body>"""
    h = h.replace('</body>', flick, 1)
    return h

for name, fn in (('a2', a_build), ('b2', b_build), ('c2', c_build), ('d2', d_build), ('e2', e_build)):
    open(f'{D}/site/{name}.html', 'w').write(fn())
import subprocess;subprocess.run(['python3',f'{D}/backbtn.py']+[f'{D}/site/{n}.html' for n in ('a2','b2','c2','d2','e2')])
print('ok')
