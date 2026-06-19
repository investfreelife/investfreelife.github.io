/* Харланметалл — движок каталога (данные: data/cats.json + data/products.json) */
(function(){
  var DATA={cats:null,prods:null,childOf:{},bySlug:{},catById:{}};
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
      a[0].forEach(function(c){DATA.bySlug[c.s]=c;DATA.catById[c.id]=c;if(c.p)(DATA.childOf[c.p]=DATA.childOf[c.p]||[]).push(c.id);});
      return DATA;
    });
    return window.__catP;
  }
  function descendants(cid){var out=[cid],st=[cid];while(st.length){var x=st.pop();(DATA.childOf[x]||[]).forEach(function(c){out.push(c);st.push(c);});}return out;}
  function prodsInCat(cid){var set={};descendants(cid).forEach(function(c){set[c]=1;});return DATA.prods.filter(function(p){return set[p.c];});}
  function ancestry(cid){var ch=[],c=DATA.catById[cid];while(c){ch.unshift(c);c=c.p?DATA.catById[c.p]:null;}return ch;}
  /* чистые характеристики (без JSON) */
  function attrs(p){var a=[];
    if(p.d)a.push('Ø'+p.d+' мм'); if(p.sq)a.push(p.sq+' мм'); if(p.t)a.push('ст. '+p.t+' мм');
    if(p.w)a.push('шир. '+p.w+' мм'); if(p.l)a.push('L '+p.l+' мм'); if(p.g)a.push(esc(p.g));
    if(p.vid)a.push(esc(p.vid)); if(!a.length&&p.note)a.push(esc(p.note));
    return a;
  }
  function priceHtml(p){return p.p?('от '+fmt(p.p)+' ₽'):'Цена <small>по запросу</small>';}
  function card(p){
    var img=p.img?'<img src="'+esc(p.img)+'" alt="'+esc(p.n)+'" loading="lazy">':'<div class="noimg" aria-hidden="true">⬡</div>';
    return '<a class="pcard" href="product.html?id='+p.i+'"><div class="ph">'+img+'</div><div class="bd"><h3>'+esc(p.n)+'</h3>'+
      '<div class="attrs">'+attrs(p).map(function(x){return '<span>'+x+'</span>';}).join('')+'</div>'+
      '<div class="pr">'+priceHtml(p)+'</div><span class="pbtn">Подробнее</span></div></a>';
  }
  function crumbs(parts){return '<nav class="crumbs" aria-label="Хлебные крошки">'+parts.map(function(p,i){
    return (i?'<span class="sep">/</span>':'')+(p.href?'<a href="'+p.href+'">'+esc(p.t)+'</a>':'<span>'+esc(p.t)+'</span>');
  }).join('')+'</nav>';}

  function renderCatalog(el){
    var tops=DATA.cats.filter(function(c){return !c.p && c.cnt>0;}).sort(function(a,b){return b.cnt-a.cnt;});
    var html=crumbs([{t:'Главная',href:'index.html'},{t:'Каталог'}])+
      '<div class="kick">Каталог</div><h1 style="font-family:Oswald;font-weight:700;font-size:clamp(28px,4.4vw,50px);text-transform:uppercase;letter-spacing:.5px">Каталог металлопроката</h1>'+
      '<p class="lead">'+fmt(DATA.prods.length)+' позиций в '+tops.length+' категориях. Выберите раздел или воспользуйтесь поиском.</p><div class="catcards">';
    tops.forEach(function(c){html+='<a class="catcard" href="category.html?cat='+encodeURIComponent(c.s)+'"><span class="ic">'+(c.ic||'⬡')+'</span><h3>'+esc(c.n)+'</h3><span class="cnt">'+fmt(c.cnt)+' позиций →</span></a>';});
    el.innerHTML=html+'</div>';
  }

  /* ===== ФАСЕТЫ ===== */
  function gv(k){return function(p){return p[k];};}
  var FDEFS=[
    {k:'_sub',label:'Раздел',get:function(p){var c=DATA.catById[p.c];return c?c.n:null;}},
    {k:'g',label:'Марка стали',get:gv('g')},
    {k:'d',label:'Диаметр, мм',num:1,get:gv('d')},
    {k:'t',label:'Толщина / стенка, мм',num:1,get:gv('t')},
    {k:'sq',label:'Сечение, мм',get:gv('sq')},
    {k:'w',label:'Ширина, мм',num:1,get:gv('w')},
    {k:'l',label:'Длина, мм',num:1,get:gv('l')},
    {k:'_ral',label:'Цвет (RAL)',get:function(p){var m=(p.n||'').match(/RAL\s?(\d{3,4})/i);return m?'RAL '+m[1]:null;}},
    {k:'_dn',label:'Типоразмер D, мм',num:1,get:function(p){var m=(p.n||'').match(/\bD\s?(\d{2,4})\b/);return m?parseInt(m[1]):null;}},
    {k:'_sz',label:'Размер',get:function(p){var m=(p.n||'').match(/\b(\d{2,4}\/\d{2,4})\b/);return m?m[1]:null;}},
    {k:'gost',label:'ГОСТ / стандарт',get:gv('gost')},
    {k:'vid',label:'Вид',get:gv('vid')},
    {k:'coat',label:'Покрытие',get:gv('coat')},
    {k:'surf',label:'Поверхность',get:gv('surf')},
    {k:'p',label:'Цена, ₽',num:1,get:gv('p')}
  ];
  function buildFacets(items){
    var out=[];
    FDEFS.forEach(function(d){
      var vals={},getf=d.get;
      items.forEach(function(p){var v=getf(p);if(v!=null&&v!=='')vals[v]=(vals[v]||0)+1;});
      var keys=Object.keys(vals);
      if(keys.length<2)return;
      if(d.num)keys.sort(function(a,b){return parseFloat(a)-parseFloat(b);});
      else keys.sort(function(a,b){return vals[b]-vals[a];});
      out.push({k:d.k,label:d.label,num:d.num,get:getf,vals:keys,counts:vals,range:d.num&&keys.length>26});
    });
    return out;
  }
  function renderCategory(el){
    var slug=qs('cat'); var c=DATA.bySlug[slug];
    if(!c){el.innerHTML='<section style="padding-top:40px"><div class="wrap"><p class="lead">Категория не найдена. <a href="catalog.html">Открыть каталог</a></p></div></section>';return;}
    var items=prodsInCat(c.id);
    var subs=(DATA.childOf[c.id]||[]).map(function(id){return DATA.catById[id];}).filter(function(x){return x&&x.cnt>0;});
    var anc=ancestry(c.id);
    var cr=[{t:'Главная',href:'index.html'},{t:'Каталог',href:'catalog.html'}];
    anc.forEach(function(a,i){cr.push(i<anc.length-1?{t:a.n,href:'category.html?cat='+encodeURIComponent(a.s)}:{t:a.n});});
    var facets=buildFacets(items);
    var fmap={};facets.forEach(function(f){fmap[f.k]=f;});
    var sel={}, rng={};
    var subHtml=subs.length?('<div class="poplinks" style="margin-top:16px"><span class="pl-label">Подразделы:</span>'+subs.map(function(s){return '<a href="category.html?cat='+encodeURIComponent(s.s)+'">'+esc(s.n)+' ('+s.cnt+')</a>';}).join('')+'</div>'):'';
    // панель фасетов
    var fh='';
    facets.forEach(function(f){
      fh+='<div class="facet" data-k="'+f.k+'"><h4>'+esc(f.label)+'</h4>';
      if(f.range){
        fh+='<div class="range"><input type="number" placeholder="от" data-r="min" data-k="'+f.k+'"><input type="number" placeholder="до" data-r="max" data-k="'+f.k+'"></div>';
      } else {
        var show=f.vals.slice(0,8), hid=f.vals.slice(8);
        fh+='<div class="opts'+(f.vals.length>6?' scroll':'')+'">';
        f.vals.forEach(function(v,i){fh+='<label'+(i>=8?' class="hid" style="display:none"':'')+'><input type="checkbox" data-k="'+f.k+'" value="'+esc(v)+'"> <span>'+esc(v)+'</span><span class="c">'+f.counts[v]+'</span></label>';});
        fh+='</div>';
        if(hid.length)fh+='<span class="more" data-k="'+f.k+'">+ ещё '+hid.length+'</span>';
      }
      fh+='</div>';
    });
    var head=crumbs(cr)+'<div class="kick">'+(anc.length>1?esc(anc[anc.length-2].n):'Каталог')+'</div>'+
      '<h1 style="font-family:Oswald;font-weight:700;font-size:clamp(26px,4.2vw,46px);text-transform:uppercase;letter-spacing:.5px">'+esc(c.n)+'</h1>'+
      '<p class="lead">'+fmt(items.length)+' позиций. Реальные характеристики и наличие. Резка под размер, доставка по РФ.</p>'+subHtml;
    var layout='<button class="ftoggle" id="ftoggle">⚙ Фильтры</button>'+
      '<div class="catlayout">'+
      (facets.length?('<aside class="facets" id="facets">'+fh+'</aside>'):'<aside></aside>')+
      '<div><div class="fbar"><span class="cnt" id="fcnt"></span>'+
        '<div style="display:flex;gap:10px;align-items:center">'+
        (facets.length?'<span class="reset" id="freset">Сбросить</span>':'')+
        '<select id="fsort"><option value="">По названию</option><option value="d">Диаметр ↑</option><option value="t">Толщина ↑</option><option value="p">Цена ↑</option></select>'+
        '<select id="fpp"><option>48</option><option>96</option><option>24</option></select></div></div>'+
        '<div id="grid" class="pgrid"></div><div id="pager" class="pager"></div>'+
        '<div style="margin-top:30px"><a class="hbtn" href="tel:'+PHONE+'">Запросить цену и наличие</a></div>'+
      '</div></div>';
    el.innerHTML='<section style="padding-top:30px"><div class="wrap">'+head+layout+'</div></section>';
    var state={sort:'',pp:48,page:1};
    function pass(p){
      for(var k in sel){if(sel[k].size){var vv=fmap[k]?fmap[k].get(p):p[k];if(!sel[k].has(String(vv)))return false;}}
      for(var k2 in rng){var r=rng[k2];var v=parseFloat(fmap[k2]?fmap[k2].get(p):p[k2]);if(r.min!=null&&!(v>=r.min))return false;if(r.max!=null&&!(v<=r.max))return false;}
      return true;
    }
    function draw(){
      var arr=items.filter(pass);
      if(state.sort==='d')arr.sort(function(a,b){return (a.d||1e9)-(b.d||1e9);});
      else if(state.sort==='t')arr.sort(function(a,b){return (a.t||1e9)-(b.t||1e9);});
      else if(state.sort==='p')arr.sort(function(a,b){return (a.p||1e12)-(b.p||1e12);});
      else arr.sort(function(a,b){return a.n.localeCompare(b.n,'ru');});
      var pages=Math.max(1,Math.ceil(arr.length/state.pp));
      if(state.page>pages)state.page=pages;
      document.getElementById('fcnt').textContent='Найдено: '+fmt(arr.length);
      document.getElementById('grid').innerHTML=arr.slice((state.page-1)*state.pp,state.page*state.pp).map(card).join('')||'<p class="lead">Под фильтры ничего не подошло. Сбросьте часть условий.</p>';
      var pg='';
      if(pages>1){
        pg+='<button data-pg="'+(state.page-1)+'" '+(state.page<=1?'disabled':'')+'>←</button>';
        for(var i=1;i<=pages;i++){if(i<=2||i>pages-2||Math.abs(i-state.page)<=1)pg+='<button data-pg="'+i+'" class="'+(i===state.page?'cur':'')+'">'+i+'</button>';else if(i===3||i===pages-2)pg+='<span>…</span>';}
        pg+='<button data-pg="'+(state.page+1)+'" '+(state.page>=pages?'disabled':'')+'>→</button>';
      }
      document.getElementById('pager').innerHTML=pg;
      document.querySelectorAll('#pager button[data-pg]').forEach(function(b){b.onclick=function(){var x=+b.dataset.pg;if(x>=1&&x<=pages){state.page=x;draw();window.scrollTo({top:0});}};});
    }
    // обработчики фасетов
    el.querySelectorAll('.facet input[type=checkbox]').forEach(function(cb){cb.onchange=function(){
      var k=cb.dataset.k; sel[k]=sel[k]||new Set();
      if(cb.checked)sel[k].add(cb.value);else sel[k].delete(cb.value);
      state.page=1; draw();
    };});
    el.querySelectorAll('.facet input[type=number]').forEach(function(inp){inp.oninput=function(){
      var k=inp.dataset.k; rng[k]=rng[k]||{min:null,max:null};
      var v=inp.value===''?null:parseFloat(inp.value); rng[k][inp.dataset.r]=v; state.page=1; draw();
    };});
    el.querySelectorAll('.facet .more').forEach(function(m){m.onclick=function(){
      m.previousElementSibling.querySelectorAll('.hid').forEach(function(l){l.style.display='flex';}); m.style.display='none';
    };});
    var fr=document.getElementById('freset'); if(fr)fr.onclick=function(){sel={};rng={};el.querySelectorAll('.facet input').forEach(function(i){if(i.type==='checkbox')i.checked=false;else i.value='';});state.page=1;draw();};
    var fs=document.getElementById('fsort'); fs.onchange=function(){state.sort=fs.value;draw();};
    var fp=document.getElementById('fpp'); fp.onchange=function(){state.pp=+fp.value;state.page=1;draw();};
    var ft=document.getElementById('ftoggle'),fc=document.getElementById('facets'); if(ft&&fc)ft.onclick=function(){fc.classList.toggle('open');};
    draw();
    document.title=c.n+' — купить в Москве, цены и наличие | Харланметалл';
  }

  function renderProduct(el){
    var id=qs('id'); var p=null;
    for(var i=0;i<DATA.prods.length;i++){if(String(DATA.prods[i].i)===id){p=DATA.prods[i];break;}}
    if(!p){el.innerHTML='<section style="padding-top:40px"><div class="wrap"><p class="lead">Товар не найден. <a href="catalog.html">Открыть каталог</a></p></div></section>';return;}
    var c=DATA.catById[p.c]; var anc=c?ancestry(c.id):[];
    var cr=[{t:'Главная',href:'index.html'},{t:'Каталог',href:'catalog.html'}];
    anc.forEach(function(a){cr.push({t:a.n,href:'category.html?cat='+encodeURIComponent(a.s)});}); cr.push({t:p.n});
    var img=p.img?'<img src="'+esc(p.img)+'" alt="'+esc(p.n)+'">':'<div class="noimg big" aria-hidden="true">⬡</div>';
    function row(k,v){return v?'<tr><td>'+k+'</td><td>'+esc(v)+'</td></tr>':'';}
    var specs=row('Марка / сплав',p.g)+row('Диаметр',p.d?p.d+' мм':'')+row('Сечение',p.sq?p.sq+' мм':'')+row('Толщина / стенка',p.t?p.t+' мм':'')+row('Ширина',p.w?p.w+' мм':'')+row('Длина',p.l?p.l+' мм':'')+row('Вид',p.vid)+row('Покрытие',p.coat)+row('Поверхность',p.surf)+row('ГОСТ / стандарт',p.gost||'по сортаменту')+row('Особенности',p.note)+row('Единица',p.u||'кг / м')+row('Наличие','на складе в Москве');
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

  function renderSearch(){
    var box=document.getElementById('searchResults'); if(!box)return;
    var input=document.getElementById('sq');
    function run(q){
      q=(q||'').trim().toLowerCase();
      if(q.length<2){box.innerHTML='<p class="lead">Введите запрос — например «труба 57», «лист 10», «нержавейка», «круг ст45».</p>';return;}
      var toks=q.split(/\s+/);
      var res=DATA.prods.filter(function(p){var s=(p.n+' '+(p.g||'')+' '+(p.gost||'')+' '+(p.d||'')+' '+(p.t||'')).toLowerCase();return toks.every(function(t){return s.indexOf(t)>=0;});});
      box.innerHTML='<p class="lead" style="margin-bottom:18px">Найдено: '+fmt(res.length)+'</p>'+(res.length?'<div class="pgrid">'+res.slice(0,60).map(card).join('')+'</div>'+(res.length>60?'<p class="lead" style="margin-top:18px">Показаны первые 60 — уточните запрос.</p>':''):'<p class="lead">Ничего не найдено. Попробуйте короче.</p>');
    }
    if(input)input.addEventListener('input',function(){run(input.value);});
    var q0=qs('q'); if(q0&&input)input.value=q0; run(q0);
  }
  function boot(){
    var el=document.getElementById('catApp');
    var page=el?el.getAttribute('data-page'):(document.getElementById('searchResults')?'search':null);
    if(!page)return;
    if(el)el.innerHTML='<section style="padding-top:40px"><div class="wrap"><p class="lead">Загружаем каталог…</p></div></section>';
    load().then(function(){
      if(page==='catalog')renderCatalog(el);
      else if(page==='category')renderCategory(el);
      else if(page==='product')renderProduct(el);
      else if(page==='search')renderSearch();
    }).catch(function(){if(el)el.innerHTML='<div class="wrap"><p class="lead">Не удалось загрузить каталог. Обновите страницу.</p></div>';});
  }
  if(document.readyState!=='loading')boot();else document.addEventListener('DOMContentLoaded',boot);
})();
