// themes
localStorage.setItem('theme', 'dark');
var light = document.getElementById('light');
var dark = document.getElementById('dark');
var x = document.getElementsByTagName('a');

light.onclick = function()
{
    document.getElementById('light_theme').style.display='block';
    document.getElementById('dark_theme').style.display='none';
    document.getElementById('main_body').style.background='rgb(209, 209, 209)';
    document.getElementById('lc').style.color='black';
    document.getElementById('sc').style.color='black';
    document.getElementById('copyright').style.color='black';
    dark.style.display='block';
    light.style.display='none';
    for(var i=0; i<x.length; i++)
    {
        document.getElementsByTagName('a')[i].style.color='black';
    }
    localStorage.setItem('theme','light');
}

dark.onclick = function()
{
    document.getElementById('light_theme').style.display='none';
    document.getElementById('dark_theme').style.display='block';
    document.getElementById('main_body').style.background='black';
    document.getElementById('lc').style.color='rgb(209, 209, 209)';
    document.getElementById('sc').style.color='rgb(209, 209, 209)';
    document.getElementById('copyright').style.color='rgb(209, 209, 209)';
    dark.style.display='none';
    light.style.display='block';
    for(var i=0; i<x.length; i++)
    {
        document.getElementsByTagName('a')[i].style.color='rgb(209, 209, 209)';
    }
    localStorage.setItem('theme','dark');
}

// sign_up --- login
var register = document.getElementById('register-btn');

register.onclick = function()
{
    // concole.log("clicked");
    document.getElementById('sc').style.display='block';
    document.getElementById('lc').style.display='none';
}
var register = document.getElementById('login-btn');

register.onclick = function()
{
    // concole.log("clicked");
    document.getElementById('lc').style.display='block';
    document.getElementById('sc').style.display='none';
}

// theme
var theme = localStorage.getItem('theme');
if(theme=='dark')
{
    document.getElementById('light_theme').style.display='none';
    document.getElementById('dark_theme').style.display='block';
    document.getElementById('main_body').style.background='black';
    document.getElementById('lc').style.color='rgb(209, 209, 209)';
    document.getElementById('sc').style.color='rgb(209, 209, 209)';
    document.getElementById('copyright').style.color='rgb(209, 209, 209)';
    dark.style.display='none';
    light.style.display='block';
    for(var i=0; i<x.length; i++)
    {
        document.getElementsByTagName('a')[i].style.color='rgb(209, 209, 209)';
    }
    localStorage.setItem('theme','dark');
}
else if(theme=='light')
{
    document.getElementById('light_theme').style.display='block';
    document.getElementById('dark_theme').style.display='none';
    document.getElementById('main_body').style.background='rgb(209, 209, 209)';
    document.getElementById('lc').style.color='black';
    document.getElementById('sc').style.color='black';
    document.getElementById('copyright').style.color='black';
    dark.style.display='block';
    light.style.display='none';
    for(var i=0; i<x.length; i++)
    {
        document.getElementsByTagName('a')[i].style.color='black';
    }
    localStorage.setItem('theme','light');
}
else
{
    document.getElementById('light_theme').style.display='none';
    document.getElementById('dark_theme').style.display='block';
    document.getElementById('main_body').style.background='black';
    document.getElementById('lc').style.color='rgb(209, 209, 209)';
    document.getElementById('sc').style.color='rgb(209, 209, 209)';
    document.getElementById('copyright').style.color='rgb(209, 209, 209)';
    dark.style.display='none';
    light.style.display='block';
    for(var i=0; i<x.length; i++)
    {
        document.getElementsByTagName('a')[i].style.color='rgb(209, 209, 209)';
    }
    localStorage.setItem('theme','dark');
}