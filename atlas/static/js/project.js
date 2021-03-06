//IIFE
(function(){

/******** Utility functions ********/

var hasId = function(element) {
  return !!$( element ).attr("id");
};


var hasType = function(element, type) {
  return $( element ).attr("id").indexOf(type) != -1;
}


function postSkill(element, append) {

  $( element ).find(':input').each(function(){
    if (hasId(this) && hasType(this, "skill")) {

        name = $( this ).attr("name");
        value = $( this ).val();

        var jsonObj = {};
        jsonObj[name] = value;

        var json = JSON.stringify(jsonObj);

        $.post("/skills/api/skill_create/", json).success(function(json){
          console.log(json);

          if (append) {
            location.reload();
          }
        });

    }
  });
}


function postTask(element, skill, append) {

  var jsonObj = {};

  $( element ).find(':input').each(function(){

    if (hasId(this) && hasType(this, "task")) {

      name = $( this ).attr("name");
      value = $( this ).val();

      if (name == "completion_time") {
        value = value + ":00";
      }

      jsonObj[name] = value;

    }
  });

  jsonObj['skill'] = skill;
  var json = JSON.stringify(jsonObj);

  $.post("/skills/api/task_create/", json).success(function(json){
    console.log(json);

    // If the form is on the overview page, append a new row to the current skill display table
    if (append) {

      var row =  "<tr><td>" + jsonObj["name"] + "</td><td>" + jsonObj["completion_time"].substring(0,5) + "</td></tr>";

      $( element ).parent().find("table").append(row);

    }

  });

}


function completeListTask(element) {

  $(element).find("p").css('text-decoration', 'line-through');
  $(element).find("p").addClass("list_task_completed");

  var task_id = $(element).find("p").attr('id');

  setToken();

  var jsonObj = {};
  jsonObj['id'] = task_id;
  jsonObj['completed'] = 'True';

  var json = JSON.stringify(jsonObj);

  $.post("/skills/api/listtask_complete/", json).success(function(json){
    console.log(json);
  });

}


function setToken() {

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


/******** Setup form handler ********/

(function(){
  var dayObj = {};

  $( "form.setup" ).on( "submit", function( event ) {

    setToken();

    postSkill(this);

    $( this ).find(':input').each(function(){
      if (hasId(this) && hasType(this, "day")) {

          var name = $( this ).attr("name");
          var value = $( this ).val() + ":00";

          dayObj[name] = value;

      };
    });

    var skill = $(this).find('#skill').val();

    $( this ).find("p").each(function(){

      postTask(this, skill);

    });

    json = JSON.stringify(dayObj);
    $.post("/skills/api/days_create/", json).success(function(json){
      console.log(json);
    });

  });
})();

/******** Overview form handlers ********/

// Existing skill task handler

$( "form.overview_task" ).on( "submit", function( event ) {

  event.preventDefault();

  setToken();

  var skill = $(this).parent().find(".skill_header").text();
  postTask(this, skill, true);

  this.reset();

});


// New skill handler

$( "form.overview_skill" ).on( "submit", function( event ) {

  event.preventDefault();

  setToken();

  postSkill(this, true);

  var skill = $(this).find('#skill').val();
  $( this ).find("p").each(function(){

    postTask(this, skill);

  });

});


// Edit day handler

(function(){
  var clicked = false;

  $( ".days th, .times td" ).on( "click", function() {

      if (!clicked) {
      var day = $(this).closest('table').find('th').eq($(this).index()).text();
      var time = $(this).closest('table').find('td').eq($(this).index()).text();

      $(this).replaceWith("<form method='POST' action='' class='day_form'><input id='" + day + "' type='time' value='0" + time.substring(0,4) + "'><input type='submit' value='Save'></form>");

      clicked = true;
    }

  });
})();

$( "table.days_times" ).on( "submit", "form.day_form", function(event) {

  event.preventDefault();

  var day = $(this).find("input").attr('id').toLowerCase();
  var time = $(this).find("input").val() + ":00";

  setToken();

  var jsonObj = {};

  jsonObj['day'] = day;
  jsonObj['time'] = time;

  json = JSON.stringify(jsonObj);

  $.post("/skills/api/days_update/", json).success(function(json){

    console.log(json);
    $("form.day_form").replaceWith("<td>" + time + "</td>");
    clicked = false;

  });

});


/******** List handler ********/

$(".list_task").on('swipe', function(event) {

  var completed = $(this).find("p").hasClass("list_task_completed");

  if (!completed && event.direction === 'left') {

    completeListTask(this);

  }

});

$(".list_task").on('click', function() {

  var completed = $(this).find("p").hasClass("list_task_completed");

  if (!completed) {

    completeListTask(this);

  }

});

})();
