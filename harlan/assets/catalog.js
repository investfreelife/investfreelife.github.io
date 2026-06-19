/* Харланметалл — движок каталога (данные: data/cats.json + data/products.json) */
(function(){
  var DATA={cats:null,prods:null,byId:null,childOf:{},bySlug:{}};
  var PHONE='+74993253969', TG='https://t.me/harlansteel';
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function fmt(n){return String(n).replace(/\B(?=(\d{3})+(?!\d))/g,' ');}
  function qs(k){return new URLSearchParams(location.search).get(k)||'';}

  function load(){
    if(window.__catP) return window.__catP;
    window.__catP=Promise.all([
      fetch('data/cats.json').then(function(r){return r.json();}),
      fetch('data/products.json').then(function(r){return r.json();})
    ]).then(function(a){
      DATA.cats=a[0]; DATA.prods=a[1];
      DATA.byCat={};
      a[0].forEach(function(c){DATA.bySlug[c.s]=c; DATA.byId=DATA.byId||{}; });
      DATA.catById={}; a[0].forEach(function(c){DATA.catById[c.id]=c; if(c.p){ (DATA.childOf[c.p]=DATA.childOf[c.p]||[]).push(c.id);} });
      return DATA;
    });
    return window.__catP;
  }
  function descendants(cid){var out=[cid],stack=[cid];while(stack.length){var x=stack.pop();(DATA.childOf[x]||[]).forEach(function(c){out.push(c);stack.push(c);});}return out;}
  function prodsInCat(cid){var set={};descendants(cid).forEach(function(c){set[c]=1;});return DATA.prods.filter(function(p){return set[p.c];});}
  function ancestry(cid){var ch=[],c=DATA.catById[cid];while(c){ch.unshift(c);c=c.p?DATA.catById[c.p]:null;}return ch;}
  function attrs(p){var a=[];if(p.d)a.push('Ø'+p.d+' мм');if(p.g)a.push(esc(p.g));if(p.dim)a.push(esc(p.dim));if(p.t)a.push(p.t+' мм');if(p.l)a.push('L'+p.l);return a;}
  function priceHtml(p){return p.p?('от '+fmt(p.p)+' ₽'):'Цена <small>по запросу</small>';}
  function card(p){
    var img=p.img?'<img src="'+esc(p.img)+'" alt="'+esc(p.n)+'" loading="lazy">':'<div class="noimg" aria-hidden="true">⬡</div>';
    return '<a class="pcard" href="product.html?id='+p.i+'"><div class="ph">'+img+'</div><div class="bd"><h3>'+esc(p.n)+'</h3>'+
      '<div class="attrs">'+attrs(p).map(function(x){return '<span>'+x+'</span>';}).join('')+'</div>'+
      '<div class="pr">'+priceHtml(p)+'</div><span class="pbtn">Подробнее</span></div></a>';
  }
  function crumbs(parts){return '<nav class="crumbs" aria-label="Хлебные крошки">'+parts.map(function(p,i){
    var sep=i?'<span class="sep">/</span>':'';
    return sep+(p.href?'<a href="'+p.href+'">'+esc(p.t)+'</a>':'<span>'+esc(p.t)+'</span>');
  }).join('')+'</nav>';}

  /* ---------- CATALOG INDEX ---------- */
  function renderCatalog(el){
    var tops=DATA.cats.filter(function(c){return !c.p && c.cnt>0;}).sort(function(a,b){return b.cnt-a.cnt;});
    var html=crumbs([{t:'Главная',href:'index.html'},{t:'Каталог'}])+
      '<div class="kick">Каталог</div><h1 style="font-family:Oswald;font-weight:700;font-size:clamp(28px,4.4vw,50px);text-transform:uppercase;letter-spacing:.5px">Каталог металлопроката</h1>'+
      '<p class="lead">'+fmt(DATA.prods.length)+' позиций в '+tops.length+' категориях. Выберите раздел или воспользуйтесь поиском.</p>'+
      '<div class="catcards">';
    tops.forEach(function(c){
      html+='<a class="catcard" href="category.html?cat='+encodeURIComponent(c.s)+'"><span class="ic">'+(c.ic||'⬡')+'</span><h3>'+esc(c.n)+'</h3><span class="cnt">'+fmt(c.cnt)+' позиций →</span></a>';
    });
    html+='</div>';
    el.innerHTML=html;
  }

  /* ---------- CATEGORY ---------- */
  function renderCategory(el){
    var slug=qs('cat'); var c=DATA.bySlug[slug];
    if(!c){el.innerHTML='<p class="lead">Категория не найдена. <a href="catalog.html">Открыть каталог</a></p>';return;}
    var items=prodsInCat(c.id);
    var subs=(DATA.childOf[c.id]||[]).map(function(id){return DATA.catById[id];}).filter(function(x){return x&&x.cnt>0;});
    var anc=ancestry(c.id);
    var cr=[{t:'Главная',href:'index.html'},{t:'Каталог',href:'catalog.html'}];
    anc.forEach(function(a,i){cr.push(i<anc.length-1?{t:a.n,href:'category.html?cat='+encodeURIComponent(a.s)}:{t:a.n});});
    var grades=[];items.forEach(function(p){if(p.g&&grades.indexOf(p.g)<0)grades.push(p.g);});grades.sort();
    var head=crumbs(cr)+'<div class="kick">'+(anc.length>1?esc(anc[anc.length-2].n):'Каталог')+'</div>'+
      '<h1 style="font-family:Oswald;font-weight:700;font-size:clamp(26px,4.2vw,46px);text-transform:uppercase;letter-spacing:.5px">'+esc(c.n)+'</h1>'+
      '<p class="lead">'+fmt(items.length)+' позиций. Реальные характеристики и наличие. Резка под размер, доставка по РФ.</p>';
    if(subs.length){head+='<div class="poplinks" style="margin-top:18px"><span class="pl-label">Подразделы:</span>'+subs.map(function(s){return '<a href="category.html?cat='+encodeURIComponent(s.s)+'">'+esc(s.n)+' ('+s.cnt+')</a>';}).join('')+'</div>';}
    if(grades.length>1){head+='<div class="filterbar"><label class="fl">Марка<select id="fgrade"><option value="">Все марки</option>'+grades.map(function(g){return '<option>'+esc(g)+'</option>';}).join('')+'</select></label>'+
      '<label class="fl">Сортировка<select id="fsort"><option value="">По названию</option><option value="d">По диаметру</option></select></label>'+
      '<label class="fl">На странице<select id="fpp"><option>48</option><option>96</option><option>24</option></select></label></div>';}
    head+='<div id="grid" class="pgrid" style="margin-top:24px"></div><div id="pager" class="pager"></div>'+
      '<div style="margin-top:30px"><a class="hbtn" href="tel:'+PHONE+'">Запросить цену и наличие</a></div>';
    el.innerHTML='<section style="padding-top:30px"><div class="wrap">'+head+'</div></section>';
    // фильтрация+пагинация
    var state={grade:'',sort:'',pp:48,page:1};
    function draw(){
      var arr=items.slice();
      if(state.grade)arr=arr.filter(function(p){return p.g===state.grade;});
      if(state.sort==='d')arr.sort(function(a,b){return (a.d||0)-(b.d||0);});
      else arr.sort(function(a,b){return a.n.localeCompare(b.n,'ru');});
      var pages=Math.max(1,Math.ceil(arr.length/state.pp));
      if(state.page>pages)state.page=pages;
      var slice=arr.slice((state.page-1)*state.pp,state.page*state.pp);
      document.getElementById('grid').innerHTML=slice.map(card).join('')||'<p class="lead">Ничего не найдено.</p>';
      var pg='';
      if(pages>1){
        pg+='<button data-pg="'+(state.page-1)+'" '+(state.page<=1?'disabled':'')+'>←</button>';
        for(var i=1;i<=pages;i++){if(i<=2||i>pages-2||Math.abs(i-state.page)<=1){pg+='<button data-pg="'+i+'" class="'+(i===state.page?'cur':'')+'">'+i+'</button>';}else if(i===3||i===pages-2){pg+='<span>…</span>';}}
        pg+='<button data-pg="'+(state.page+1)+'" '+(state.page>=pages?'disabled':'')+'>→</button>';
      }
      document.getElementById('pager').innerHTML=pg;
      document.querySelectorAll('#pager button[data-pg]').forEach(function(b){b.onclick=function(){var n=+b.dataset.pg;if(n>=1&&n<=pages){state.page=n;draw();window.scrollTo({top:0});}};});
    }
    var fg=document.getElementById('fgrade'),fs=document.getElementById('fsort'),fp=document.getElementById('fpp');
    if(fg)fg.onchange=function(){state.grade=fg.value;state.page=1;draw();};
    if(fs)fs.onchange=function(){state.sort=fs.value;draw();};
    if(fp)fp.onchange=function(){state.pp=+fp.value;state.page=1;draw();};
    draw();
    document.title=c.n+' — купить в Москве, цены и наличие | Харланметалл';
  }

  /* ---------- PRODUCT ---------- */
  function renderProduct(el){
    var id=qs('id'); var p=null;
    for(var i=0;i<DATA.prods.length;i++){if(DATA.prods[i].i===id){p=DATA.prods[i];break;}}
    if(!p){el.innerHTML='<p class="lead">Товар не найден. <a href="catalog.html">Открыть каталог</a></p>';return;}
    var c=DATA.catById[p.c]; var anc=c?ancestry(c.id):[];
    var cr=[{t:'Главная',href:'index.html'},{t:'Каталог',href:'catalog.html'}];
    anc.forEach(function(a){cr.push({t:a.n,href:'category.html?cat='+encodeURIComponent(a.s)});});
    cr.push({t:p.n});
    var img=p.img?'<img src="'+esc(p.img)+'" alt="'+esc(p.n)+'">':'<div class="noimg big" aria-hidden="true">⬡</div>';
    function row(k,v){return v?'<tr><td>'+k+'</td><td>'+esc(v)+'</td></tr>':'';}
    var specs=row('Марка / сплав',p.g)+row('Диаметр',p.d?p.d+' мм':'')+row('Толщина',p.t?p.t+' мм':'')+row('Длина',p.l?p.l+' мм':'')+row('Размеры',p.dim)+row('ГОСТ',p.gost||'по сортаменту')+row('Единица',p.u||'кг / м')+row('Наличие','на складе в Москве');
    var price=p.p?('<span class="big">от '+fmt(p.p)+' ₽</span>'):'<span class="big">Цена по запросу</span>';
    var rel=c?prodsInCat(c.id).filter(function(x){return x.i!==p.i;}).slice(0,5):[];
    el.innerHTML='<section style="padding-top:30px"><div class="wrap">'+crumbs(cr)+
      '<div class="pdp"><div class="pdp-media">'+img+'</div><div class="pdp-info">'+
      '<h1>'+esc(p.n)+'</h1>'+(p.g?'<span class="pdp-grade">Марка '+esc(p.g)+'</span>':'')+
      '<table class="specs">'+specs+'</table>'+
      '<div class="pdp-price">'+price+'<span style="color:var(--mut);font-size:14px">актуальная цена и остаток — по позиции</span></div>'+
      '<div class="pdp-cta"><a class="btn-lg btn-gold" href="tel:'+PHONE+'">Запросить цену</a><a class="btn-lg btn-ghost" href="'+TG+'" target="_blank" rel="noopener">Уточнить в Telegram</a></div>'+
      '</div></div>'+
      (rel.length?'<div style="margin-top:48px"><div class="kick">Похожие позиции</div><h2 class="h2" style="margin-bottom:6px">'+(c?esc(c.n):'')+'</h2><div class="pgrid">'+rel.map(card).join('')+'</div></div>':'')+
      '</div></section>';
    document.title=p.n+(p.g?' '+p.g:'')+' — купить | Харланметалл';
  }

  /* ---------- SEARCH ---------- */
  function renderSearch(el){
    var box=document.getElementById('searchResults'); if(!box)return;
    var input=document.getElementById('sq');
    function run(q){
      q=(q||'').trim().toLowerCase();
      if(q.length<2){box.innerHTML='<p class="lead">Введите запрос — например «труба 57», «лист 10», «нержавейка», «круг ст45».</p>';return;}
      var toks=q.split(/\s+/);
      var res=DATA.prods.filter(function(p){var s=(p.n+' '+(p.g||'')+' '+(p.gost||'')).toLowerCase();return toks.every(function(t){return s.indexOf(t)>=0;});});
      box.innerHTML='<p class="lead" style="margin-bottom:18px">Найдено: '+fmt(res.length)+'</p>'+(res.length?'<div class="pgrid">'+res.slice(0,60).map(card).join('')+'</div>'+(res.length>60?'<p class="lead" style="margin-top:18px">Показаны первые 60. Уточните запрос.</p>':''):'<p class="lead">Ничего не найдено. Попробуйте короче.</p>');
    }
    if(input){input.addEventListener('input',function(){run(input.value);});}
    var q0=qs('q'); if(q0&&input){input.value=q0;} run(q0);
  }

  /* ---------- ROUTER ---------- */
  function boot(){
    var el=document.getElementById('catApp');
    var page=el?el.getAttribute('data-page'):(document.getElementById('searchResults')?'search':null);
    if(!page)return;
    if(el)el.innerHTML='<section style="padding-top:40px"><div class="wrap"><p class="lead">Загружаем каталог…</p></div></section>';
    load().then(function(){
      if(page==='catalog')renderCatalog(el);
      else if(page==='category')renderCategory(el);
      else if(page==='product')renderProduct(el);
      else if(page==='search')renderSearch(el);
    }).catch(function(e){if(el)el.innerHTML='<div class="wrap"><p class="lead">Не удалось загрузить каталог. Обновите страницу.</p></div>';});
  }
  if(document.readyState!=='loading')boot();else document.addEventListener('DOMContentLoaded',boot);
})();
