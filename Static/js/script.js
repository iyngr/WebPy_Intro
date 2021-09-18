// Wait until the page has fully loaded before applying the script
$(document).ready(function () {
    // Bind a function to the submit form
    $(document).on("submit", "#registerr", function (e) {
        // Prevent the default form post behavior to prevent the page from reloading
        e.preventDefault();

        // Get the form data
        var form = $('#registerr').serialize();

        // Send an ajax request over to the route /postregisteration
        $.ajax({
            url: '/postregisteration',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response);

            }
        });
    });

        $(document).on("submit", "#loginform", function (e) {
        // Prevent the default form post behavior to prevent the page from reloading
        e.preventDefault();
        // Get the form data
        var form = $(this).serialize();

        $.ajax({
            url: '/checklogin',
            type: 'POST',
            data: form,
            success: function (res) {
                if(res == 'error'){
                    alert('Could not login')
                }else{
                    console.log('Log in as',res)
                    window.location.href = '/';
                }
            }
        });
    });

    $(document).on('click','#logout', function(e){

    e.preventDefault();

    $.ajax({
        url : '/logout',
        type : 'GET',
        success : function(res){
            if (res == 'success'){
              alert('Log out') ;
              window.location.href = '/login'
            }else{
               alert('Something Wrong!')
            }
        }
    });
});

$(document).on('click','#delete', function(e){

    e.preventDefault();
    form = $('#deleteid').serialize();
    $.ajax({
        url : '/deletepost',
        type : 'POST',
        data : form,
        success : function(res){
            if (res == 'success'){
              alert('Delete') ;
              window.location.reload();
            }else{
               alert('Something Wrong!')
            }
        }
    });
});
    $(document).on('submit','#post-activity', function(e){

    e.preventDefault();
    form = $(this).serialize();
    $.ajax({
        url : '/postactivie',
        type : 'POST',
        data : form ,
        success : function(res){
            console.log(res)
             window.location.reload();
        }
    });
});

    $(document).on('submit','#exper-form', function(e){

    e.preventDefault();
    form = $(this).serialize();
    $.ajax({
        url : '/postexper',
        type : 'POST',
        data : form ,
        success : function(res){
            console.log(res)
        }
    });
});

$(document).on('submit','#setting-form', function(e){

    e.preventDefault();
    form = $(this).serialize();
    $.ajax({
        url : '/update-settings',
        type : 'POST',
        data : form ,
        success : function(res){
            if(res == ' success'){
                window.location.href = window.location.href
            }else{
                alert(res)
            }
        }
    });
});

$(document).on('submit','#comment-activity', function(e){

    e.preventDefault();
    form = $(this).serialize();
    $.ajax({
        url : '/comment-activity',
        type : 'POST',
        data : form ,
        dataType : 'json' ,
        success : function(res){
                window.location.href = window.location.href

        }
    });
});

$(document).on('keyup','#search', function(e){



        // Retrieve the input field text and reset the count to zero
        var filter = $(this).val(), count = 0;

        // Loop through the comment list
        $(".card-body.post p").each(function(){

            // If the list item does not contain the text phrase fade it out
            if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).parent().parent().fadeOut();
                    console.log('fade')
            // Show the list item if the phrase matches and increase the count by 1
            } else {
                $(this).parent().parent().show();
                count++;
            }
             var numberItems = count;
             console.log(numberItems)
        });



});
});