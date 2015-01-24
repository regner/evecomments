
$(document).ready(function(){
    $('.ssoLogin').click(function(event){
        event.preventDefault();

        var url         = $(this).attr('href');
        var window_name = 'popUp';
        var window_size = $(this).data('popup');

        window.open(url, window_name, window_size)
    });

    window.onresize = function(){
        parent.postMessage(document.body.offsetHeight, '*');
    };
})

function closeAndRefreshParent(){
    window.opener.location.reload();
    window.close();
}