$(document).on('click', '.panel-heading span.glyphicon-plus', function (e) {
    var $this = $(this);
    if (!$this.hasClass('panel-collapse')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapse');
    	$this.removeClass('glyphicon-plus').addClass('glyphicon-minus');
       
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapse');
         $this.removeClass('glyphicon-minus').addClass('glyphicon-plus');
    }
});