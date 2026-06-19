(function(){
  var t='light';try{t=localStorage.getItem('hm-theme')||'light';}catch(e){}
  document.documentElement.setAttribute('data-theme',t);
  window.hmToggleTheme=function(){
    var cur=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
    document.documentElement.setAttribute('data-theme',cur);
    try{localStorage.setItem('hm-theme',cur);}catch(e){}
    hmIcon();
  };
  function hmIcon(){var d=document.documentElement.getAttribute('data-theme')==='dark';
    document.querySelectorAll('[data-theme-icon]').forEach(function(e){e.textContent=d?'☀':'☾';e.parentNode.setAttribute('title',d?'Светлая тема':'Тёмная тема');});}
  if(document.readyState!=='loading')hmIcon();else document.addEventListener('DOMContentLoaded',hmIcon);
})();
