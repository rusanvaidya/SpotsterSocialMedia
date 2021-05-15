function myProfile()
{
    document.getElementById("mydd1").classList.toggle("show");
}
function myNotification()
{
    document.getElementById("b-n").style.display='none';
    document.getElementById("b2-i").style.display='none';
    document.getElementById("b2-a").style.display='inline-block';
    document.getElementById("mydd2").classList.toggle("show");
}
function myMessage()
{
    document.getElementById("b-m").style.display='none';
    document.getElementById("b3-i").style.display='none';
    document.getElementById("b3-a").style.display='inline-block';
    document.getElementById("mydd3").classList.toggle("show");
}


window.onclick = function(event)
{
    if (!event.target.matches('.d1btn'))
    {
        var dd1 = document.getElementsByClassName("dd1-content");
        var i;
        for (i = 0; i < dd1.length; i++)
        {
            var opendd1 = dd1[i];
            if (opendd1.classList.contains('show'))
            {
                opendd1.classList.remove('show');
            }
        }
    }
    if (!event.target.matches('.d2btn')) {
        var dd2 = document.getElementsByClassName("dd2-content");
        var i;
        for (i = 0; i < dd2.length; i++)
        {
            var opendd2 = dd2[i];
            if (opendd2.classList.contains('show'))
            {
                document.getElementById("b2-i").style.display='inline-block';
                document.getElementById("b2-a").style.display='none';
                opendd2.classList.remove('show');
            }
        }
    }
    if (!event.target.matches('.d3btn'))
    {
        var dd3 = document.getElementsByClassName("dd3-content");
        var i;
        for (i = 0; i < dd3.length; i++)
        {
            var opendd3 = dd3[i];
            if (opendd3.classList.contains('show'))
            {
                document.getElementById("b3-i").style.display='inline-block';
                document.getElementById("b3-a").style.display='none';
                opendd3.classList.remove('show');
            }
        }
    }
    if (!event.target.matches('.post-drop'))
    {
        var pdrop = document.getElementsByClassName("about-post");
        var i;
        for (i = 0; i < pdrop.length; i++)
        {
            var openpd = pdrop[i];
            if (openpd.classList.contains('show'))
            {
                openpd.classList.remove('show');
            }
        }
    }
    if (!event.target.matches('.emdisp'))
    {
        if (document.getElementById("emobox").classList.contains('show_emoji'))
        {
          document.getElementById("emobox").classList.remove('show_emoji');
        }
    }
}

function loader_feed()
{
    document.getElementById('h-i').style.display='none';
    document.getElementById('h-a').style.display='inline-block';
}
function loader_video()
{
    document.getElementById('v-i').style.display='none';
    document.getElementById('v-a').style.display='inline-block';
}
function loader_trending()
{
    document.getElementById('t-i').style.display='none';
    document.getElementById('t-a').style.display='inline-block';
}
function loader_discover()
{
    document.getElementById('d-i').style.display='none';
    document.getElementById('d-a').style.display='inline-block';
}
function show_side_nav()
{
    document.getElementById('m-n-i').style.display='none';
    document.getElementById('m-n-a').style.display='inline-block';
    document.getElementById('side_nav').style.display='block';
}
