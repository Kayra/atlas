// Create a skill from the skill form
// $( "form.setup" ).on( "submit", function( event ) {

//   var data = $( this ).serializeObject();
//   var json = JSON.stringify(data);
//   var csrftoken = getCookie('csrftoken');

//   $.ajaxSetup({
//     contentType: "application/json; charset=utf-8",
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
//             // Send the token to same-origin, relative URLs only.
//             // Send the token only if the method warrants CSRF protection
//             // Using the CSRFToken value acquired earlier
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

// $.post("/skills/api/skill_create/", json).success(function(json){
//     console.log(json);
//   });
// });

var dayObj = new Object();

$( "form.setup" ).on( "submit", function( event ) {

  event.preventDefault();

  var csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
      contentType: "application/json; charset=utf-8",
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
              // Send the token to same-origin, relative URLs only.
              // Send the token only if the method warrants CSRF protection
              // Using the CSRFToken value acquired earlier
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  var skill;

  $( this ).find(':input').each(function(){
    if ($( this ).attr("id") && $( this ).attr("id").indexOf("skill") != -1) {

        name = $( this ).attr("name");
        value = $( this ).val();

        skill = value;

        var jsonObj = {};
        jsonObj[name] = value;

        json = JSON.stringify(jsonObj);

        $.post("/skills/api/skill_create/", json).success(function(json){
          console.log(json);
        });

    } else if ($( this ).attr("id") && $( this ).attr("id").indexOf("day") != -1) {

        var name = $( this ).attr("name");
        var value = $( this ).val();

        dayObj[name] = value;

    };
  });

  $( this ).find("p").each(function(){

    var jsonObj = {};

    $( this ).find(':input').each(function(){

      name = $( this ).attr("name");
      value = $( this ).val();

      jsonObj[name] = value;

    });

    jsonObj['skill'] = skill;
    json = JSON.stringify(jsonObj);
    $.post("/skills/api/task_create/", json).success(function(json){
      console.log(json);
    });

  });

  json = JSON.stringify(dayObj);
  console.log(json);

});



/* Utility functions */
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.fn.serializeObject = function()
{
   var o = {};
   var a = this.serializeArray();
   $.each(a, function() {
       if (o[this.name]) {
           if (!o[this.name].push) {
               o[this.name] = [o[this.name]];
           }
           o[this.name].push(this.value || '');
       } else {
           o[this.name] = this.value || '';
       }
   });
   return o;
};
