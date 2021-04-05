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
}
  
var loader_icon = document.getElementById('pre-loader');
var toload_div = document.getElementById('div-loaded');
var change1 =function()
{
    loader_icon.classList.toggle('not-loaded');
}
var change2 = function()
{
    toload_div.classList.remove('not-loaded');
}
function loader_feed()
{
    document.getElementById('h-i').style.display='none';
    document.getElementById('h-a').style.display='inline-block';
    setTimeout(change1, 200);
    setTimeout(change2, 300);
}
function loader_video()
{
    document.getElementById('v-i').style.display='none';
    document.getElementById('v-a').style.display='inline-block';
    setTimeout(change1, 200);
    setTimeout(change2, 300);
}
function loader_trending()
{
    document.getElementById('t-i').style.display='none';
    document.getElementById('t-a').style.display='inline-block';
    setTimeout(change1, 200);
    setTimeout(change2, 300);
}
function loader_discover()
{
    document.getElementById('d-i').style.display='none';
    document.getElementById('d-a').style.display='inline-block';
    setTimeout(change1, 200);
    setTimeout(change2, 300);
}
function loader()
{
    setTimeout(change1, 200);
    setTimeout(change2, 300);    
}

function show_side_nav()
{
    document.getElementById('m-n-i').style.display='none';
    document.getElementById('m-n-a').style.display='inline-block';
    document.getElementById('side_nav').style.display='block';
}