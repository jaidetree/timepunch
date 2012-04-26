(function($){
    $(document).ready(function(){
        $('a.clock-in').on('click', function(){
            var href = $(this).attr('href');
            $.getJSON(href, function(data, textStatus, jqXHR){
                if( data.status == "success" )
                {
                    window.location.reload();
                }
            });
            return false;
        });
        $('form.clock-out').on('submit', function(){
            var href = $(this).attr('action');
            var form_data = $(this).serialize();
            $.post(href, form_data, function(data, textStatus, jqXHR){
                if( data.status == "success" )
                {
                    window.location.reload();
                }
            });
            return false;
        });

        $('table.times .delete').on('click', function(){
            var href = $(this).attr('href'), 
                element = $(this).parents('tr');
            var answer = confirm("Are you sure you want to delete this entry?");
            if( ! answer )
            {
                return false;
            }
            $.ajax({ 
                type: 'delete',
                url: href,
                data: {},
                beforeSend: function(jqXHR) {
                    jqXHR.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                },
                success: function(data){
                    if( data.status != "success" )
                    {
                        alert( data.message );
                        return false;
                    }

                    $(element).addClass('removed').fadeOut(1500);
                }
            });
            return false;
        });

        if( ! $('.clock-out').length )
        {
            return false;
        }
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        setInterval(function(){
            var seconds = 0;
            var minutes = 0;
            var hours = 0;
            var days = 0;
            var time = parseInt(Date.now()/1000);

            var initial_diff = time - parseInt($('.elapsed').data('started'));
            seconds = initial_diff;
            days = parseInt(seconds / (3600 * 24));
            seconds -= days * (3600 * 24);
            hours = parseInt(seconds / 3600);
            seconds -= hours * 3600;
            minutes = parseInt(seconds / 60);
            seconds -= minutes * 60;

            return function(){
                var string = "";
                seconds++;
                string = seconds + " sec";

                if( seconds > 59 )
                {
                    minutes++;
                    seconds -= 59;
                }
                if( minutes > 59 )
                {
                    hours++;
                    minutes -= 59;
                }
                if( hours > 23 )
                {
                    days++;                    
                    hours -= 23;
                }
                if( minutes > 0 )
                {
                    string = minutes + " min " + string;
                }
                if( hours > 0 )
                {
                    string = hours + " hours " + string;
                }
                if( days > 0 )
                {
                    string = days + " days " + string;
                }
                $('.elapsed').text(string);                
            };
        }(), 1000);
    });
})(jQuery);
