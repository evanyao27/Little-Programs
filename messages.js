// Paste this in messages.htm right before </head>      <script src="messages.js"></script>

document.addEventListener("DOMContentLoaded", function(event) { 
    var threads = document.getElementsByClassName('thread'); 

    console.log(threads.length);

    var ids = []; 
    var names = []

    for (var i = 0; i < threads.length; i++)
    {
        // var start = threads[i].innerHTML.indexOf("Evan")
        // var end = threads[i].innerHTML.indexOf("\n\n");

        var stuff = threads[i].innerHTML; 
        var end = stuff.indexOf('<');
        var id = stuff.substring(0,end);
        names.push(id);
        id = id.replace(/\s+/g, '_'); 
        ids.push(id); 

        threads[i].id = id; 
    }

    console.log(threads.length);

    var nav = document.getElementsByClassName('nav')[0]; 

    var html = "<img src='../photos/profile.jpg'> <ul>"; 

    for (var i = 0; i < ids.length; i++)
    {

        html += "<li>  <a href='#" + ids[i]  +" '>" + names[i]  +" </li>";
    }

    html += "</ul>";

    nav.innerHTML = html; 
  });