
$(document).ready(function(){
    $('.ssoLogin').click(function(event){
        event.preventDefault();

        var $this = $(this);

        var url = $this.attr('href');
        var windowName = 'popUp';
        var windowSize = $this.data('popup');

        window.open(url, windowName, windowSize)
    })
})

function closeAndRefreshParent(){
    window.opener.location.reload();
    window.close();
}