// ==UserScript==
// @name         newsdigest in disguise
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the world!
// @author       You
// @match        https://newsdigest.jp/pages/coronavirus/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
    if(document.cookie.indexOf('ref=nd_app') == -1){
        document.cookie = 'ref=nd_app';
        location.reload();
    }


    function _x(){
        var cs = document.querySelectorAll('circle[id]');
        var facis = [];


        cs.forEach(
            function(e){
                facis.push(e.__data__);
            }
        );

        console.log(facis);
        //console.log(JSON.stringify(facis, null, 4));
        var js = JSON.stringify(facis);
        var form1 = document.createElement('form');
        form1.method = 'POST';
        form1.target = '_blank';
        form1.action = 'https://script.google.com/macros/s/AKfycbxu8CJ-bNEnnxjLye0AJebjof0IGM2OxasIYBB4cMyZahAUNABp/exec';
        form1.innerHTML = `<textarea name="j">${js}</textarea>`;
        document.body.appendChild(form1);
        form1.submit();

    }
    window._x = _x;

    var div = document.createElement('div');
    div.innerHTML = `
<style>
#mybutton{
position: sticky;
bottom:10%;
right: 20%;
position:fixed;
background: red;
color: white;
width: 15%;
height: 15%;
font-size: 40px;
font-weight: bold;
text-align: center;
z-index: 1000;
}
</style>
<button id="mybutton" onclick="_x();">
CLICK
</button>
`;
    document.body.appendChild(div);

})();