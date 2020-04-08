// ==UserScript==
// @name         newsdigest in disguise
// @namespace    http://tampermonkey.net/
// @version      0.1
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

})();