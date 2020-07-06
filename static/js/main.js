/*Textbox Events*/
$(document).on('focusin', 'nav input.search-textbox', function(){
    if($(this).val() <= 0){
        var parent = $(this).closest('form.search');
        parent.addClass('focused');
    }
});
$(document).on('focusout', 'nav input.search-textbox', function(){
    if($(this).val() <= 0){
        var parent = $(this).closest('form.search');
        parent.removeClass('focused');
    }
});
$(document).on('click', 'nav .search', function(){
    $(this).children('input.search-textbox').focus();
});

/*Text Key Events for Animating Icons i.e. .ico-btn*/
$(document).on('keyup', 'nav input.search-textbox', function(){
    var parent = $(this).closest('form.search');
    var phrase = $(this).val(),
        phrase_length = phrase.length;

    if(phrase_length >= 2){
        parent.addClass('multi-char');
        if(!parent.hasClass('not-null')){
            parent.addClass('not-null');
        }

    }
    else if(phrase_length == 1){
        parent.addClass('not-null');
        parent.removeClass('multi-char');
    }
    else if(phrase_length <= 0){
        parent.removeClass('not-null');
        parent.removeClass('multi-char');
    }
});