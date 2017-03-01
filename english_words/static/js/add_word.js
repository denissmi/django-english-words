$(document).ready(function(){
    $('#new_english_word').keyup(function(){
        if($(this).val() && $('#new_russian_word').val())
            $('#add_word_button').prop('disabled', false);
        else
            $('#add_word_button').prop('disabled', true);
    });

    $('#new_russian_word').keyup(function(){
        if($(this).val() && $('#new_english_word').val())
            $('#add_word_button').prop('disabled', false);
        else
            $('#add_word_button').prop('disabled', true);
    });

    $("#new_english_word").keypress(function(e){
        var symbol = (e.which) ? e.which : e.keyCode;
        if (symbol !== 8 && symbol !== 32 && symbol !== 45 && ( symbol < 97 || symbol > 122))  return false;
    });
});