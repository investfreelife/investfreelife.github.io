# -*- coding: utf-8 -*-
import json
D=json.load(open('/tmp/harlan-build/_catalog_data.json',encoding='utf-8'))
cat=D['category']; prods=D['products']

NAV=[("catalog.html","Каталог"),("constructions.html","Конструкции"),("ai-search.html","AI-подбор"),
     ("delivery.html","Доставка"),("about.html","О нас"),("contacts.html","Контакты")]
def header(active):
    parts=[]
    for h,l in NAV:
        cls=' class="active"' if h==active else ''
        parts.append('<a href="'+h+'"'+cls+'>'+l+'</a>')
    links="".join(parts)
    return f'''<div class="topbar"><div class="wrap"><div class="in">
  <span>Металлопрокат по ГОСТ · Москва и вся Россия</span>
  <div class="r"><span>Пн–Пт 9:00–18:00</span><span>Оплата с НДС · безнал</span><a href="tel:+74993253969">+7 499 325-39-69</a></div>
</div></div></div>
<header><div class="wrap"><nav>
  <a class="brand" href="index.html"><span class="mk" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 12l9 4 9-4M3 17l9 4 9-4"/></svg></span>ХАРЛАН<span class="gold">МЕТАЛЛ</span></a>
  <div class="navlinks">{links}</div>
  <div class="spacer"></div>
  <a class="hphone gold" href="tel:+74993253969">+7 499 325-39-69</a>
  <a class="hbtn" href="ai-search.html">Подобрать металл</a>
</nav></div></header>'''
FOOTER=open('/tmp/harlan-build/_shared.html',encoding='utf-8').read().split('<!-- CALLBAR -->')[1]
FOOTER='<div class="callbar">'+FOOTER.split('<div class="callbar">')[1]
# rebuild footer+callbar cleanly from _shared
sh=open('/tmp/harlan-build/_shared.html',encoding='utf-8').read()
CALLBAR=sh[sh.index('<div class="callbar">'):sh.index('<!-- FOOTER -->')].strip()
FOOT=sh[sh.index('<footer>'):].strip()
FOOTER=FOOT+"\n"+CALLBAR
SCRIPT='''<script>
var io=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}})},{threshold:.1});
document.querySelectorAll('.reveal').forEach(function(e){io.observe(e)});
</script>'''
def shell(fn,title,desc,body):
    html=f'''<!DOCTYPE html>
<html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#0a0a10">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css"></head><body>
{header("catalog.html")}
<main>{body}</main>
{FOOTER}
{SCRIPT}</body></html>'''
    open('/tmp/harlan-build/'+fn,'w',encoding='utf-8').write(html); print(fn,len(html),'bytes')

def attr(p):
    a=[]
    if p.get('diameter'): a.append(f"Ø{int(p['diameter']) if float(p['diameter']).is_integer() else p['diameter']} мм")
    if p.get('steel_grade'): a.append(p['steel_grade'])
    lo=p.get('length_options') or p.get('length')
    if lo: a.append(f"L {int(float(lo)) if str(lo).replace('.','').isdigit() else lo} мм")
    return a

# ===== LIST =====
cards=""
for p in prods:
    chips="".join(f"<span>{x}</span>" for x in attr(p))
    cards+=f'''<a class="pcard reveal" href="product.html">
  <div class="ph"><img src="{p['image_url']}" alt="{p['name']}" loading="lazy"></div>
  <div class="bd"><h3>{p['name']}</h3><div class="attrs">{chips}</div>
  <div class="pr">Цена <small>по запросу</small></div>
  <span class="pbtn">Запросить цену</span></div></a>'''
grades=sorted({p['steel_grade'] for p in prods if p.get('steel_grade')})
list_body=f'''<section style="padding-top:30px"><div class="wrap">
  <nav class="crumbs reveal" aria-label="Хлебные крошки"><a href="catalog.html">Каталог</a><span class="sep">/</span><a href="{cat['url']}">Цветные металлы</a><span class="sep">/</span><span>{cat['name']}</span></nav>
  <div class="kick reveal">Цветные металлы</div>
  <h1 class="reveal" style="font-family:Oswald;font-weight:700;font-size:clamp(30px,4.6vw,52px);text-transform:uppercase;letter-spacing:.5px">{cat['name']}</h1>
  <p class="lead reveal">{len(prods)} позиций с реальными фото, размерами и наличием. Марки {", ".join(grades)}. Резка под размер, доставка по РФ.</p>
  <div class="filterbar reveal" role="search" aria-label="Фильтры">
    <label class="fl">Марка<select aria-label="Марка">{"".join(f"<option>{g}</option>" for g in ["Все марки"]+grades)}</select></label>
    <label class="fl">Диаметр, мм<select aria-label="Диаметр"><option>Любой</option><option>7</option><option>20</option><option>50</option><option>95</option><option>150</option></select></label>
    <label class="fl">Длина, мм<select aria-label="Длина"><option>Любая</option><option>2000</option><option>3000</option></select></label>
    <label class="fl">Наличие<select aria-label="Наличие"><option>В наличии</option><option>Под заказ</option></select></label>
  </div>
  <div class="pgrid">{cards}</div>
  <div class="reveal" style="margin-top:34px;padding:22px;border:1px solid var(--line2);border-radius:14px;background:var(--bg2);display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
    <div style="color:var(--soft);font-size:15px">Это раздел каталога Харланметалл. Полный каталог — 16 000+ позиций в 23 категориях.</div>
    <a class="hbtn" href="{cat['url']}">Открыть на сайте</a>
  </div>
</div></section>'''
shell("catalog-category.html",f"{cat['name']} — купить в Москве, цены и наличие | Харланметалл",
      f"{cat['name']}: {len(prods)} позиций с фото, размерами и наличием. Марки {', '.join(grades)}. Резка под размер, доставка по России, оплата с НДС.",list_body)

# ===== PDP =====
p=prods[0]
rel=""
for r in prods[1:6]:
    rel+=f'''<a class="pcard reveal" href="product.html"><div class="ph"><img src="{r['image_url']}" alt="{r['name']}" loading="lazy"></div><div class="bd"><h3>{r['name']}</h3><div class="attrs">{"".join(f"<span>{x}</span>" for x in attr(p))}</div><div class="pr">Цена <small>по запросу</small></div></div></a>'''
def row(k,v): return f"<tr><td>{k}</td><td>{v}</td></tr>" if v else ""
specs=row("Марка сплава",p.get('steel_grade') or p.get('material'))
specs+=row("Диаметр",f"{int(p['diameter']) if p.get('diameter') and float(p['diameter']).is_integer() else p.get('diameter')} мм" if p.get('diameter') else "")
lo=p.get('length_options') or p.get('length')
specs+=row("Длина",f"{int(float(lo))} мм" if lo else "")
specs+=row("ГОСТ",p.get('gost') or "по сортаменту")
specs+=row("Единица",p.get('unit') or "кг / м")
specs+=row("Состояние","пресс / полутвёрдый")
specs+=row("Наличие","на складе в Москве")
pdp_body=f'''<section style="padding-top:30px"><div class="wrap">
  <nav class="crumbs reveal" aria-label="Хлебные крошки"><a href="catalog.html">Каталог</a><span class="sep">/</span><a href="{cat['url']}">Цветные металлы</a><span class="sep">/</span><a href="catalog-category.html">{cat['name']}</a><span class="sep">/</span><span>{p['name']}</span></nav>
  <div class="pdp">
    <div class="pdp-media reveal"><img src="{p['image_url']}" alt="{p['name']}"></div>
    <div class="pdp-info reveal">
      <h1>{p['name']}</h1>
      <span class="pdp-grade">Марка {p.get('steel_grade') or '—'}</span>
      <table class="specs">{specs}</table>
      <div class="pdp-price"><span class="big">Цена по запросу</span><span style="color:var(--mut);font-size:14px">актуальная цена и остаток — по позиции</span></div>
      <div class="pdp-cta">
        <a class="btn-lg btn-gold" href="tel:+74993253969">Запросить цену</a>
        <a class="btn-lg btn-ghost" href="https://t.me/harlansteel">Уточнить в Telegram</a>
      </div>
      <div class="b2b" style="grid-template-columns:1fr 1fr;margin-top:24px">
        <div class="x"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 3h9l5 5v13H5z"/></svg><div><b>Резка под размер</b><small>готовим к отгрузке</small></div></div>
        <div class="x"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h13v10H3z"/><path d="M16 10h4l1 3v4h-5z"/><circle cx="6.5" cy="17.5" r="1.5"/><circle cx="17.5" cy="17.5" r="1.5"/></svg><div><b>Доставка по РФ</b><small>от склада в Москве</small></div></div>
      </div>
    </div>
  </div>
  <div style="margin-top:54px"><div class="kick reveal">Похожие позиции</div><h2 class="h2 reveal" style="margin-bottom:6px">{cat['name']}</h2>
  <div class="pgrid">{rel}</div></div>
</div></section>'''
shell("product.html",f"{p['name']} {('Ø'+str(int(p['diameter'])) if p.get('diameter') and float(p['diameter']).is_integer() else '')} {p.get('steel_grade') or ''} — купить | Харланметалл",
      f"{p['name']} марка {p.get('steel_grade') or ''}: фото, размеры, наличие на складе в Москве. Резка под размер, доставка по России, оплата с НДС. Запросить цену: +7 499 325-39-69.",pdp_body)
print("OK")
