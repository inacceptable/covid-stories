
window.onload = function(){
  document.getElementById('shareBtn').onclick = function() {
  FB.ui({
    display: 'popup',
    method: 'share',
    href: 'https://developers.facebook.com/docs/',
  }, function(response){});
  }
}