# -*- coding: utf-8 -*-
import io

NAV = [("catalog.html","Каталог"),("constructions.html","Конструкции"),("ai-search.html","AI-подбор"),
       ("delivery.html","Доставка"),("about.html","О нас"),("contacts.html","Контакты")]

def header(active):
    links=""
    for href,label in NAV:
        cls=' class="active"' if href==active else ''
        links+=f'<a href="{href}"{cls}>{label}</a>'
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

FOOTER='''<footer><div class="wrap">
  <div class="foot">
    <div>
      <a class="brand" href="index.html"><span class="mk" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M3 12l9 4 9-4M3 17l9 4 9-4"/></svg></span>ХАРЛАН<span class="gold">МЕТАЛЛ</span></a>
      <p>B2B-маркетплейс металлопроката: единый каталог остатков поставщиков, AI-подбор и поставка по ГОСТ по всей России.</p>
    </div>
    <div><h4>Каталог</h4><a href="https://www.harlansteel.ru/catalog">Металлопрокат</a><a href="https://www.harlansteel.ru/constructions">Готовые конструкции</a><a href="catalog.html">Все категории</a><a href="https://www.harlansteel.ru/catalog/truby">Трубы</a><a href="https://www.harlansteel.ru/catalog/metizy">Метизы</a></div>
    <div><h4>Компания</h4><a href="ai-search.html">AI-подбор</a><a href="delivery.html">Доставка и оплата</a><a href="about.html">О компании</a><a href="suppliers.html">Поставщикам</a><a href="contacts.html">Контакты</a></div>
    <div><h4>Контакты</h4><a href="tel:+74993253969">+7 499 325-39-69</a><a href="mailto:info@harlansteel.ru">info@harlansteel.ru</a><a href="https://t.me/harlansteel" target="_blank" rel="noopener">Telegram: @harlansteel</a><span class="fi">Москва · доставка по РФ</span><span class="fi">Пн–Пт 9:00–18:00</span></div>
  </div>
  <div class="legal">
    <span>© 2026 Харланметалл · Металлопрокат по ГОСТ · ИНН / ОГРН — реквизиты по запросу</span>
    <span>Цены не являются публичной офертой</span>
  </div>
</div></footer>
<div class="callbar">
  <a class="c2" href="https://t.me/harlansteel" target="_blank" rel="noopener">Telegram</a>
  <a class="c1" href="tel:+74993253969">Позвонить</a>
</div>'''

SCRIPT='''<script>
var io=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}})},{threshold:.12,rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.reveal').forEach(function(e){io.observe(e)});
</script>'''

def page(fn, active, title, desc, body):
    html=f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a0a10">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{FOOTER}
{SCRIPT}
</body>
</html>'''
    open('/tmp/harlan-build/'+fn,'w',encoding='utf-8').write(html)
    print(fn, len(html),'bytes')

# ============ CATALOG ============
catalog='''<section class="phero"><img class="bg" src="assets/s2.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">Каталог</div>
  <h1 class="reveal">Каталог проката <span class="gradtext">и конструкций</span></h1>
  <p class="reveal">Более 16 000 позиций в 23 категориях. Реальные остатки, цены и фото поставщиков — в каталоге на сайте.</p>
  <div class="trust">
    <div class="t"><div><b>16 000+</b><small>позиций</small></div></div>
    <div class="t"><div><b>23</b><small>категории</small></div></div>
    <div class="t"><div><b>ГОСТ</b><small>сертификаты</small></div></div>
    <div class="t"><div><b>РФ</b><small>доставка</small></div></div>
  </div></div></section>
<section><div class="wrap">
  <div class="pillars">
    <a class="pillar reveal" href="https://www.harlansteel.ru/catalog"><span class="arr">↗</span><div class="ic">🏗️</div><h3>Металлопрокат</h3><p>Листовой и сортовой прокат, трубы, метизы, нержавеющая и цветные металлы, качественные и износостойкие стали.</p><span class="more">Открыть раздел →</span></a>
    <a class="pillar reveal" href="https://www.harlansteel.ru/constructions"><span class="arr">↗</span><div class="ic">🏛️</div><h3>Готовые конструкции</h3><p>Ангары, навесы, заборы, каркасы зданий, лестницы, козырьки, контейнерные площадки и МАФ — под ключ.</p><span class="more">Открыть раздел →</span></a>
  </div>
  <div class="poplinks reveal"><span class="pl-label">Популярное:</span>
    <a href="https://www.harlansteel.ru/catalog/listovoy-prokat">Листовой прокат</a>
    <a href="https://www.harlansteel.ru/catalog/sortovoy-prokat">Сортовой прокат</a>
    <a href="https://www.harlansteel.ru/catalog/truby">Трубы</a>
    <a href="https://www.harlansteel.ru/catalog/metizy">Метизы</a>
    <a href="https://www.harlansteel.ru/catalog/nerzhaveyuschaya-stal">Нержавеющая сталь</a>
    <a href="https://www.harlansteel.ru/catalog/tsvetnye-metally">Цветные металлы</a>
  </div></div></section>
<section style="background:var(--bg2)"><div class="wrap">
  <div class="kick reveal">Как устроен каталог</div>
  <h2 class="h2 reveal">Находите позицию за секунды</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M7 12h10M10 18h4"/></svg></div><h3>Фильтры под прокат</h3><p>Марка стали, ГОСТ, типоразмер, наличие. Сужаете выборку до нужной позиции.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/></svg></div><h3>Остатки и цены</h3><p>Реальные остатки и цены поставщиков в одном окне — без «уточняйте».</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg></div><h3>AI-поиск</h3><p>Не знаете точный сортамент? Опишите словами, голосом или загрузите смету.</p></div>
  </div>
  <a class="hbtn" href="ai-search.html" style="margin-top:30px">Подобрать через AI</a>
</div></section>
<section><div class="wrap"><div class="b2b">
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg><div><b>Прокат по ГОСТ</b><small>сертификаты на партию</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 3h9l5 5v13H5z"/><path d="M8 13h8M8 17h5"/></svg><div><b>Резка под размер</b><small>готовим к отгрузке</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h13v10H3z"/><path d="M16 10h4l1 3v4h-5z"/><circle cx="6.5" cy="17.5" r="1.5"/><circle cx="17.5" cy="17.5" r="1.5"/></svg><div><b>Доставка по РФ</b><small>от склада в Москве</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg><div><b>Безнал с НДС</b><small>счёт, УПД, отсрочка</small></div></div>
</div></div></section>
<section style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s1.jpg" alt=""><div class="in">
  <h2>Весь каталог — <span class="gradtext">на сайте</span></h2>
  <p>Более 16 000 позиций с реальными остатками, ценами и фото. Откройте каталог или доверьте подбор AI.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="https://www.harlansteel.ru/catalog">Открыть полный каталог</a><a class="btn-lg btn-ghost" href="ai-search.html">Подобрать через AI</a></div>
</div></div></section>'''

# ============ CONSTRUCTIONS ============
constr_items=[("🏭","Ангары"),("⛺","Навесы"),("🚧","Заборы сварные"),("🏚️","Гаражи под ключ"),
("🏬","Склады и цеха"),("🏢","Здания из сэндвич-панелей"),("🔧","Металлоконструкции"),("🏗️","Каркасы зданий"),
("🪜","Лестницы металлические"),("☂️","Козырьки"),("🪟","Антресоли"),("📦","Контейнерные площадки"),
("🌳","МАФ для благоустройства"),("🛡️","Противоподкопные сетки")]
cl_cards="".join(f'<a class="cl reveal" href="https://www.harlansteel.ru/constructions"><div class="ic">{i}</div><h3>{n}</h3></a>' for i,n in constr_items)
constructions=f'''<section class="phero"><img class="bg" src="assets/s4.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">Готовые конструкции</div>
  <h1 class="reveal">Металлоконструкции <span class="gradtext">под ключ</span></h1>
  <p class="reveal">Проектируем, изготавливаем по ГОСТ и монтируем. Свой металл — 16 000+ позиций проката, поэтому сроки и цена от производителя.</p>
  <a class="hbtn reveal" href="#напр">Смотреть направления</a></div></section>
<section id="напр"><div class="wrap">
  <div class="kick reveal">Направления</div><h2 class="h2 reveal">Что изготавливаем</h2>
  <div class="cl-grid">{cl_cards}</div></div></section>
<section style="background:var(--bg2)"><div class="wrap">
  <div class="kick reveal">Как работаем</div><h2 class="h2 reveal">От замера до монтажа</h2>
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Замер и проект</h3><p>Выезд, обмер, проектное решение под задачу и нагрузки.</p></div>
    <div class="step reveal"><div class="n">02</div><h3>Смета</h3><p>Прозрачный расчёт по позициям и согласование объёма.</p></div>
    <div class="step reveal"><div class="n">03</div><h3>Изготовление</h3><p>Производство по ГОСТ из собственного проката с контролем качества.</p></div>
    <div class="step reveal"><div class="n">04</div><h3>Доставка и монтаж</h3><p>Привозим и собираем на объекте по Москве и регионам.</p></div>
  </div></div></section>
<section><div class="wrap"><div class="kick reveal">Почему мы</div><h2 class="h2 reveal">Конструкции без переплат</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7l9-4 9 4-9 4z"/><path d="M3 12l9 4 9-4"/></svg></div><h3>Свой металл</h3><p>16 000+ позиций проката в наличии — не закупаем на стороне, цена от производителя.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div><h3>Сроки</h3><p>Изготовление параллельно поставке металла — экономим неделями.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg></div><h3>По ГОСТ с гарантией</h3><p>Сертифицированный металл, документы, гарантия на конструкции.</p></div>
  </div></div></section>
<section style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s1.jpg" alt=""><div class="in">
  <h2>Рассчитаем <span class="gradtext">вашу конструкцию</span></h2>
  <p>Опишите задачу — подготовим решение, смету и срок. Перезвоним и поможем с выбором.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="tel:+74993253969">Позвонить · +7 499 325-39-69</a><a class="btn-lg btn-ghost" href="https://www.harlansteel.ru/constructions">Смотреть конструкции</a></div>
</div></div></section>'''

# ============ AI-SEARCH ============
aisearch='''<section class="phero"><img class="bg" src="assets/s3.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">AI-подбор</div>
  <h1 class="reveal">Опишите задачу — <span class="gradtext">найдём металл</span></h1>
  <p class="reveal">Не нужно знать точный ГОСТ и сортамент. Напишите словами, продиктуйте голосом или загрузите смету — AI распознает позиции и соберёт спецификацию.</p>
  <div class="aisearch reveal" role="search" style="margin-top:26px">
    <div class="badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/></svg> AI-подбор металлопроката</div>
    <div class="row">
      <label class="field" for="q"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input id="q" type="text" placeholder="Напр.: труба 57×3,5 ГОСТ 8732 или «лист 10мм для основания станка»" aria-label="Поиск по каталогу металлопроката"></label>
      <button class="mic" type="button" aria-label="Голосовой поиск"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></button>
      <button class="go" type="button" onclick="document.getElementById('q').focus()"><span>Найти</span> →</button>
    </div>
    <div class="chips">
      <span class="chip">труба 57×3,5 ГОСТ 8732</span><span class="chip">лист 10мм</span><span class="chip">арматура А500С 12</span><span class="chip">уголок 50×50</span><span class="chip">круг ст45</span>
    </div>
  </div></div></section>
<section><div class="wrap"><div class="kick reveal">Как работает</div><h2 class="h2 reveal">Четыре шага к спецификации</h2>
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Запрос</h3><p>Текст, голос или файл — смета, чертёж, переписка. Понимаем «человеческий» язык.</p></div>
    <div class="step reveal"><div class="n">02</div><h3>Распознавание</h3><p>AI извлекает позиции, марки, размеры и сопоставляет с каталогом по ГОСТ.</p></div>
    <div class="step reveal"><div class="n">03</div><h3>Аналоги</h3><p>Чего-то нет — предложим замену по марке и размеру, не теряя задачу.</p></div>
    <div class="step reveal"><div class="n">04</div><h3>Спецификация</h3><p>Готовый список с наличием, ценой и сроком — сразу к счёту.</p></div>
  </div></div></section>
<section style="background:var(--bg2)"><div class="wrap"><div class="kick reveal">Возможности</div><h2 class="h2 reveal">Зачем это снабженцу</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 3h9l5 5v13H5z"/></svg></div><h3>Поиск по смете</h3><p>Загрузите файл — извлечём все позиции автоматически, без ручного ввода.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg></div><h3>Голосовой ввод</h3><p>Продиктуйте позицию прямо с площадки — удобно в цеху и в дороге.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg></div><h3>Подбор аналогов</h3><p>Алгоритм знает взаимозаменяемость марок и размеров.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div><h3>Экономия времени</h3><p>Минуты вместо часов на сборку заявки из десятков позиций.</p></div>
  </div></div></section>
<section style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s3.jpg" alt=""><div class="in">
  <h2>Попробуйте <span class="gradtext">AI-подбор</span></h2>
  <p>Опишите задачу — соберём спецификацию с наличием и ценой. Это бесплатно и ни к чему не обязывает.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="https://www.harlansteel.ru/ai-search">Открыть AI-поиск</a><a class="btn-lg btn-ghost" href="tel:+74993253969">+7 499 325-39-69</a></div>
</div></div></section>'''

# ============ DELIVERY ============
delivery='''<section class="phero"><img class="bg" src="assets/s2.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">Доставка и оплата</div>
  <h1 class="reveal">Доставка по России <span class="gradtext">и оплата для бизнеса</span></h1>
  <p class="reveal">Отгружаем со склада в Москве по всей стране, режем под размер и работаем по-белому: безнал с НДС, счёт и закрывающие документы.</p></div></section>
<section><div class="wrap"><div class="kick reveal">Доставка</div><h2 class="h2 reveal">Привезём куда нужно</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h13v10H3z"/><path d="M16 10h4l1 3v4h-5z"/><circle cx="6.5" cy="17.5" r="1.5"/><circle cx="17.5" cy="17.5" r="1.5"/></svg></div><h3>Авто по Москве и РФ</h3><p>Доставка автотранспортом по городу и в регионы. Сроки и тариф — по заявке.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="5" width="16" height="11" rx="2"/><path d="M4 19h16M9 16v3M15 16v3"/></svg></div><h3>ЖД в дальние регионы</h3><p>Отправка по железной дороге для крупных и дальних поставок.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M6 21V9l6-4 6 4v12"/></svg></div><h3>Самовывоз</h3><p>Забирайте со склада в Москве — подготовим к выдаче.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 3h9l5 5v13H5z"/></svg></div><h3>Резка под размер</h3><p>Порежем прокат в размер под ваш проект перед отгрузкой.</p></div>
  </div></div></section>
<section style="background:var(--bg2)"><div class="wrap"><div class="kick reveal">Оплата</div><h2 class="h2 reveal">Удобно для юрлиц и физлиц</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg></div><h3>Безнал с НДС</h3><p>Счёт, оплата по реквизитам, полный пакет документов.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M5 3h9l5 5v13H5z"/><path d="M8 13h8M8 17h5"/></svg></div><h3>Документы</h3><p>УПД, счёт-фактура, сертификаты и паспорта на партию.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div><h3>Отсрочка</h3><p>Для постоянных клиентов — отсрочка платежа по согласованию.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><h3>Розница</h3><p>Для физлиц — наличный расчёт или картой по согласованию.</p></div>
  </div></div></section>
<section><div class="wrap"><div class="kick reveal">Порядок</div><h2 class="h2 reveal">Как проходит сделка</h2>
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Заявка</h3><p>Каталог, AI-подбор или смета.</p></div>
    <div class="step reveal"><div class="n">02</div><h3>Спецификация и счёт</h3><p>Список с наличием, ценой и сроком.</p></div>
    <div class="step reveal"><div class="n">03</div><h3>Оплата</h3><p>Безнал с НДС или отсрочка.</p></div>
    <div class="step reveal"><div class="n">04</div><h3>Резка и отгрузка</h3><p>Подготовка, доставка или самовывоз.</p></div>
  </div></div></section>
<section style="background:var(--bg2)"><div class="wrap"><div class="kick reveal" style="text-align:center;width:100%;justify-content:center">Вопросы</div><h2 class="h2 reveal" style="text-align:center">Коротко о доставке и оплате</h2>
  <div class="faq">
    <details class="qa reveal"><summary>Доставляете в регионы?</summary><div class="a">Да, по всей России — авто и ЖД. Конкретный способ, срок и стоимость рассчитываем по заявке.</div></details>
    <details class="qa reveal"><summary>Работаете с НДС?</summary><div class="a">Да, безналичный расчёт с НДС, счёт и закрывающие документы (УПД, счёт-фактура).</div></details>
    <details class="qa reveal"><summary>Можно отсрочку платежа?</summary><div class="a">Для постоянных клиентов — да, по согласованию и договору.</div></details>
    <details class="qa reveal"><summary>Режете прокат под размер?</summary><div class="a">Да, порежем в нужный размер перед отгрузкой.</div></details>
    <details class="qa reveal"><summary>Есть минимальная партия?</summary><div class="a">Работаем и оптом, и в розницу. Условия по объёму уточняйте по телефону.</div></details>
  </div></div></section>
<section style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s1.jpg" alt=""><div class="in">
  <h2>Рассчитаем <span class="gradtext">доставку и счёт</span></h2>
  <p>Назовите позиции и адрес — подготовим спецификацию, счёт и срок поставки.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="tel:+74993253969">Позвонить · +7 499 325-39-69</a><a class="btn-lg btn-ghost" href="https://t.me/harlansteel">Написать в Telegram</a></div>
</div></div></section>'''

# ============ ABOUT ============
about='''<section class="phero"><img class="bg" src="assets/s4.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">О компании</div>
  <h1 class="reveal">Металл без <span class="gradtext">посредников и догадок</span></h1>
  <p class="reveal">Харланметалл — B2B-маркетплейс металлопроката. Мы сводим остатки и цены разных поставщиков в единый каталог и помогаем закупщику найти нужную позицию через AI — быстро и по ГОСТ.</p></div></section>
<section><div class="wrap"><div class="feat">
  <div>
    <div class="kick reveal">Что мы делаем</div><h2 class="h2 reveal">Единый каталог + <span class="gradtext">AI</span></h2>
    <ul>
      <li class="reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7l9-4 9 4-9 4z"/><path d="M3 12l9 4 9-4"/></svg><span><b>Каталог остатков поставщиков.</b> 16 000+ позиций в одном окне с реальными ценами.</span></li>
      <li class="reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/></svg><span><b>AI-нормализация прайсов.</b> Приводим разрозненные прайсы к единому ГОСТ-виду.</span></li>
      <li class="reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg><span><b>AI-подбор.</b> Поиск по смете, голосу и описанию — даже без точного сортамента.</span></li>
      <li class="reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg><span><b>Поставка по ГОСТ.</b> Сертификаты, документы, доставка по всей России.</span></li>
    </ul>
  </div>
  <div class="media reveal"><img src="assets/s3.jpg" alt="Производство металлопроката"><div class="ov"></div></div>
</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="stats">
  <div class="stat reveal"><div class="n gradtext">16 000+</div><div class="l">позиций в каталоге</div></div>
  <div class="stat reveal"><div class="n gradtext">23</div><div class="l">категории проката</div></div>
  <div class="stat reveal"><div class="n gradtext">ГОСТ</div><div class="l">сертификат на партию</div></div>
  <div class="stat reveal"><div class="n gradtext">РФ</div><div class="l">доставка по стране</div></div>
</div></div></section>
<section style="background:var(--bg2)"><div class="wrap"><div class="kick reveal">Принципы</div><h2 class="h2 reveal">Во что мы верим</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><h3>Прозрачные цены</h3><p>Цены от производителя, без скрытых наценок и «уточняйте».</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg></div><h3>Качество по ГОСТ</h3><p>Сертификаты и паспорта на каждую партию.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/></svg></div><h3>Технологичность</h3><p>AI экономит часы снабженца на подборе и спецификациях.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8M8 8h8M8 16h5"/></svg></div><h3>Работа по-белому</h3><p>Договор, безнал с НДС, полный пакет документов.</p></div>
  </div></div></section>
<section><div class="wrap"><div class="b2b">
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8M8 8h8M8 16h5"/></svg><div><b>Работаем по договору</b><small>УПД, счёт-фактура, сертификаты</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.8 19.8 0 0 1 3.08 4.18 2 2 0 0 1 5.06 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg><div><b>+7 499 325-39-69</b><small>Пн–Пт 9:00–18:00</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M22 6l-10 7L2 6"/></svg><div><b>info@harlansteel.ru</b><small>Telegram: @harlansteel</small></div></div>
  <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 12l2 2 4-4"/></svg><div><b>Реквизиты</b><small>ИНН / ОГРН — по запросу</small></div></div>
</div>
  <div style="text-align:center;margin-top:34px"><a class="btn-lg btn-gold" href="https://www.harlansteel.ru/catalog">Перейти в каталог</a></div>
</div></section>'''

# ============ CONTACTS ============
contacts='''<section class="phero"><img class="bg" src="assets/s2.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">Контакты</div>
  <h1 class="reveal">Свяжитесь <span class="gradtext">с нами</span></h1>
  <p class="reveal">Подберём металл, рассчитаем доставку и выставим счёт. Отвечаем по телефону, почте и в Telegram.</p></div></section>
<section><div class="wrap"><div class="two">
  <div>
    <div class="b2b" style="grid-template-columns:1fr 1fr;margin-top:0">
      <a class="x reveal" href="tel:+74993253969"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.8 19.8 0 0 1 3.08 4.18 2 2 0 0 1 5.06 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg><div><b>+7 499 325-39-69</b><small>Пн–Пт 9:00–18:00</small></div></a>
      <a class="x reveal" href="mailto:info@harlansteel.ru"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M22 6l-10 7L2 6"/></svg><div><b>info@harlansteel.ru</b><small>почта для заявок</small></div></a>
      <a class="x reveal" href="https://t.me/harlansteel" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 3L2 10l6 3 9-7-7 9 3 6z"/></svg><div><b>@harlansteel</b><small>Telegram</small></div></a>
      <div class="x reveal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><div><b>Москва</b><small>доставка по всей России</small></div></div>
    </div>
    <div class="x reveal" style="margin-top:14px;display:block">
      <b style="display:block;margin-bottom:4px">Реквизиты</b>
      <small style="color:var(--mut)">Работаем по договору. УПД, счёт-фактура, сертификаты. ИНН / ОГРН — предоставляем по запросу.</small>
    </div>
  </div>
  <div class="reveal">
    <h2 class="h2" style="font-size:clamp(24px,3vw,34px)">Оставить заявку</h2>
    <p class="lead" style="font-size:16px;margin-bottom:18px">Опишите задачу — перезвоним и поможем с подбором.</p>
    <form class="form" action="mailto:info@harlansteel.ru" method="post" enctype="text/plain">
      <div class="f"><label for="name">Ваше имя</label><input id="name" name="name" type="text" required></div>
      <div class="f"><label for="phone">Телефон</label><input id="phone" name="phone" type="tel" required></div>
      <div class="f"><label for="email">Email</label><input id="email" name="email" type="email"></div>
      <div class="f"><label for="msg">Что нужно подобрать</label><textarea id="msg" name="message" rows="4" required></textarea></div>
      <button class="btn-lg btn-gold" type="submit">Отправить заявку</button>
    </form>
  </div>
</div></div></section>
<section style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s1.jpg" alt=""><div class="in">
  <h2>Нужен <span class="gradtext">металл</span>?</h2>
  <p>Позвоните или напишите в Telegram — подберём позицию и рассчитаем поставку.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="tel:+74993253969">Позвонить</a><a class="btn-lg btn-ghost" href="https://t.me/harlansteel">Telegram</a></div>
</div></div></section>'''

# ============ SUPPLIERS ============
suppliers='''<section class="phero"><img class="bg" src="assets/s4.jpg" alt="" aria-hidden="true">
  <div class="wrap in"><div class="kick reveal">Поставщикам</div>
  <h1 class="reveal">Продавайте металл <span class="gradtext">через Харланметалл</span></h1>
  <p class="reveal">Пришлите прайс — мы нормализуем его по ГОСТ через AI и покажем ваши позиции закупщикам в едином каталоге. Без своего сайта, SEO и ручной работы с карточками.</p>
  <a class="hbtn reveal" href="#стать">Стать поставщиком</a></div></section>
<section><div class="wrap"><div class="kick reveal">Как это работает</div><h2 class="h2 reveal">Прайс → каталог → заявки</h2>
  <div class="steps">
    <div class="step reveal"><div class="n">01</div><h3>Присылаете прайс</h3><p>Excel или любой формат — как есть. Ничего переделывать не нужно.</p></div>
    <div class="step reveal"><div class="n">02</div><h3>AI нормализует</h3><p>Приводим марки, размеры и ГОСТ к единому виду и сопоставляем с каталогом.</p></div>
    <div class="step reveal"><div class="n">03</div><h3>Витрина закупщикам</h3><p>Ваши остатки видны в каталоге и в AI-поиске тысячам B2B-покупателей.</p></div>
    <div class="step reveal"><div class="n">04</div><h3>Получаете заявки</h3><p>Закупщики находят ваши позиции — вы получаете запросы и продажи.</p></div>
  </div></div></section>
<section style="background:var(--bg2)"><div class="wrap"><div class="kick reveal">Выгоды</div><h2 class="h2 reveal">Почему это удобно</h2>
  <div class="why">
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div><h3>Новые B2B-заявки</h3><p>Поток закупщиков без вложений в сайт, рекламу и SEO.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/></svg></div><h3>AI делает рутину</h3><p>Нормализация прайса к ГОСТ-виду автоматически — без карточек вручную.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg></div><h3>AI-поиск приводит спрос</h3><p>Покупатели находят ваши позиции по смете, голосу и описанию.</p></div>
    <div class="w reveal"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8M8 8h8M8 16h5"/></svg></div><h3>Прозрачные условия</h3><p>Работа по договору, понятные правила, ваши цены и остатки.</p></div>
  </div></div></section>
<section><div class="wrap"><div class="kick reveal">Кому подходит</div><h2 class="h2 reveal">Наши партнёры</h2>
  <div class="cl-grid">
    <div class="cl reveal"><div class="ic">🏬</div><h3>Склады металлопроката</h3></div>
    <div class="cl reveal"><div class="ic">🏭</div><h3>Заводы-производители</h3></div>
    <div class="cl reveal"><div class="ic">🔁</div><h3>Трейдеры</h3></div>
    <div class="cl reveal"><div class="ic">🏗️</div><h3>Производители конструкций</h3></div>
  </div></div></section>
<section id="стать" style="padding-bottom:0"><div class="cta reveal"><img class="bg" src="assets/s1.jpg" alt=""><div class="in">
  <h2>Станьте <span class="gradtext">поставщиком</span></h2>
  <p>Пришлите прайс — подключим ваши позиции к каталогу и AI-поиску. Расскажем условия за один звонок.</p>
  <div class="btns"><a class="btn-lg btn-gold" href="tel:+74993253969">Позвонить · +7 499 325-39-69</a><a class="btn-lg btn-ghost" href="mailto:info@harlansteel.ru">Прислать прайс</a></div>
</div></div></section>'''

B="https://www.harlansteel.ru"
page("catalog.html","catalog.html","Каталог металлопроката и конструкций — Харланметалл","Каталог Харланметалл: более 16 000 позиций металлопроката и готовых конструкций. Листовой и сортовой прокат, трубы, метизы, нержавейка, цветмет. AI-подбор, цены от производителя.",catalog)
page("constructions.html","constructions.html","Готовые металлоконструкции под ключ — Харланметалл","Изготовление металлоконструкций под ключ: ангары, навесы, заборы, каркасы зданий, лестницы, козырьки, МАФ. Проект, изготовление по ГОСТ, доставка и монтаж по России.",constructions)
page("ai-search.html","ai-search.html","AI-подбор металлопроката по смете и голосу — Харланметалл","AI-подбор металлопроката: опишите задачу словами, голосом или загрузите смету — найдём позиции, подберём аналоги и соберём спецификацию с ценами и наличием.",aisearch)
page("delivery.html","delivery.html","Доставка и оплата металлопроката — Харланметалл","Доставка металлопроката по всей России: авто, ЖД, самовывоз, резка под размер. Оплата безналом с НДС, счёт и документы, отсрочка для постоянных клиентов.",delivery)
page("about.html","about.html","О компании — Харланметалл","Харланметалл — B2B-маркетплейс металлопроката: единый каталог остатков поставщиков, AI-нормализация прайсов по ГОСТ и AI-подбор. 16 000+ позиций, поставка по России.",about)
page("contacts.html","contacts.html","Контакты — Харланметалл","Контакты Харланметалл: +7 499 325-39-69, info@harlansteel.ru, Telegram @harlansteel. Москва, доставка по всей России. Пн–Пт 9:00–18:00. Оставьте заявку на подбор металла.",contacts)
page("suppliers.html",None,"Поставщикам — продавайте металл через Харланметалл","Поставщикам металлопроката: пришлите прайс — AI нормализует его по ГОСТ и покажет ваши позиции закупщикам в едином каталоге. Новые B2B-заявки без своего сайта.",suppliers)
print("OK")
