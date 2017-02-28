$(document).ready(function(){
    $('#mark_all').change(function(){
        if ($(this).prop('checked'))
            $('[type="checkbox"]').prop('checked', true);
        else
            $('[type="checkbox"]').prop('checked', false);
    });

    $('[type="checkbox"]').change(function(){
        if ($(this).prop('checked'))
            $('#delete_words_button').prop('disabled', false);
        else
            $('#delete_words_button').prop('disabled', true);
            $('[type="checkbox"]').each(function(){
                if ($(this).prop('checked'))
                    $('#delete_words_button').prop('disabled', false);
            });
    });
});