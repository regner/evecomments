(function () {
    'use strict';

    var ec_comments_uri = 'http://localhost:5000/comments/embed';

    window.onload = addIframe;

    function addIframe() {
        var comments_div = document.getElementById('evecomments_thread');
        var iframe       = document.createElement('iframe');

        iframe.setAttribute('allowTransparency', 'true');
        iframe.setAttribute('scrolling',         'no');
        iframe.setAttribute('frameBorder',       '0');
        iframe.setAttribute('src',               getCommentsUrl())

        comments_div.appendChild(iframe);
    };

    function getCommentsUrl() {
        var config    = getConfigObject();
        var urlParams = encodeQueryData(config)

        var commentsUrl = ec_comments_uri + '?' + urlParams

        return commentsUrl
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