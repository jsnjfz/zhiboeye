/**
 * Created by admin on 16/11/28.
 */
(function(window, document){
    /*jshint eqnull:true */
    'use strict';
    var bgLoad, regBgUrlEscape;
    var uniqueUrls = {};

    if(document.addEventListener){
        regBgUrlEscape = /\(|\)|'/;

        bgLoad = function (url, cb){
            var img = document.createElement('img');
            img.onload = function(){
                img.onload = null;
                img.onerror = null;
                img = null;
                cb();
            };
            img.onerror = img.onload;

            img.src = url;

            if(img && img.complete && img.onload){
                img.onload();
            }
        };

        addEventListener('lazybeforeunveil', function(e){
            var tmp, load, bg, poster;
            if(!e.defaultPrevented) {

                if(e.target.preload == 'none'){
                    e.target.preload = 'auto';
                }

                tmp = e.target.getAttribute('data-link');
                if(tmp){
                    addStyleScript(tmp, true);
                }

                // handle data-script
                tmp = e.target.getAttribute('data-script');
                if(tmp){
                    addStyleScript(tmp);
                }

                // handle data-require
                tmp = e.target.getAttribute('data-require');
                if(tmp){
                    if(lazySizes.cfg.requireJs){
                        lazySizes.cfg.requireJs([tmp]);
                    } else {
                        addStyleScript(tmp);
                    }
                }

                // handle data-bg
                bg = e.target.getAttribute('data-bg');
                if (bg) {
                    e.detail.firesLoad = true;
                    load = function(){
                        e.target.style.backgroundImage = 'url(' + (regBgUrlEscape.test(bg) ? JSON.stringify(bg) : bg ) + ')';
                        e.detail.firesLoad = false;
                        lazySizes.fire(e.target, '_lazyloaded', {}, true, true);
                    };

                    bgLoad(bg, load);
                }

                // handle data-poster
                poster = e.target.getAttribute('data-poster');
                if(poster){
                    e.detail.firesLoad = true;
                    load = function(){
                        e.target.poster = poster;
                        e.detail.firesLoad = false;
                        lazySizes.fire(e.target, '_lazyloaded', {}, true, true);
                    };

                    bgLoad(poster, load);

                }
            }
        }, false);

    }

    function addStyleScript(src, style){
        if(uniqueUrls[src]){
            return;
        }
        var elem = document.createElement(style ? 'link' : 'script');
        var insertElem = document.getElementsByTagName('script')[0];

        if(style){
            elem.rel = 'stylesheet';
            elem.href = src;
        } else {
            elem.src = src;
        }
        uniqueUrls[src] = true;
        uniqueUrls[elem.src || elem.href] = true;
        insertElem.parentNode.insertBefore(elem, insertElem);
    }
})(window, document);