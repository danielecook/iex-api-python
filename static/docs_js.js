$( document ).ready(function() {
  $("a[href^='http://'], a[href^='https://'], a[href$='pdf']").attr("target","_blank");
});