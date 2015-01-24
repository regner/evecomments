(function () {
    'use strict';

    var ec_comments_uri = 'http://{{ request.host }}/comments/embed';

    window.onload = addIframe;

    function addIframe() {
        var comments_div = document.getElementById('evecomments_thread');
        var iframe       = createIframe();

        comments_div.appendChild(iframe);

        createEventListener();

    };

    function createEventListener() {
        var event_method  = window.addEventListener ? "addEventListener" : "attachEvent";
        var eventer       = window[event_method];
        var message_event = event_method == "attachEvent" ? "onmessage" : "message";

        eventer(message_event, function(event) {
            if (event.origin !== 'http://{{ request.host }}' || isNaN(event.data)) return;
            document.getElementById('ec_iframe').style.height = event.data + 'px';
        }, false);
    };

    function createIframe() {
        var iframe = document.createElement('iframe');

        iframe.setAttribute('style',             'width: 100% !important;');
        iframe.setAttribute('title',             'EVE Comments');
        iframe.setAttribute('id',                'ec_iframe');
        iframe.setAttribute('allowTransparency', 'true');
        iframe.setAttribute('height',            '100%');
        iframe.setAttribute('width',             '100%');
        iframe.setAttribute('scrolling',         'no');
        iframe.setAttribute('frameBorder',       '0');
        iframe.setAttribute('src',               getCommentsUrl());

        return iframe
    };

    function getCommentsUrl() {
        var config     = getConfigObject();
        var url_params = encodeQueryData(config)

        return ec_comments_uri + '?' + url_params;
    };

    function getConfigObject() {
        var config = {
            'ec_site_id':      ec_site_id,
            'ec_thread_id':    ec_thread_id,
            'ec_thread_title': ec_thread_title,
            'ec_thread_url':   ec_thread_url
        }

        return config
    };

    function encodeQueryData(data) {
        var ret = [];

        for (var d in data) ret.push(encodeURIComponent(d) + "=" + encodeURIComponent(data[d]));

        return ret.join("&");
    };
}());