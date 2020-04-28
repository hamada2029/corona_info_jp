// ==UserScript==
// @name         newsdigest in disguise
// @namespace    http://tampermonkey.net/
// @version      0.5
// @description  try to take over the world!
// @author       You
// @match        https://newsdigest.jp/pages/coronavirus/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    if(document.cookie.indexOf('ref=nd_app') == -1){
        document.cookie = 'ref=nd_app';
        location.reload();
    }


    // var t=e.facility の2行前あたりにブレークポイント
    // if(!window.__x){window.__x=[]}; window.__x.push(e);

    function __postFacis(){
        var facis = [];

        window.__x.forEach(
            function(e){
                facis.push(e.facility);
            }
        );

        console.log(facis);
        var w = open('https://hamada2029.github.io/corona_info_jp/table.html?' + new Date().getTime());

        setTimeout(
            function(){
                w.postMessage(facis, 'https://hamada2029.github.io');
                console.log('postmsg');
            },
            2000
        );

    }
    window.__postFacis = __postFacis;

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
<button id="mybutton" onclick="__postFacis();">
CLICK
</button>
`;
    document.body.appendChild(div);

})();


