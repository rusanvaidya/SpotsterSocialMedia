var d_link = document.getElementById('d_links');
var n_link = document.getElementById('n_links');

function show_not()
{ 
    n_link.style.display='block';
}

function show_pp()
{
    d_link.style.display='block';
}
window.onclick = function(e) {
    if (!e.target.matches('.d_link')) {
        var dd = document.getElementById("d_links");
        if (dd.classList.contains('show')) {
            dd.classList.remove('show');
        }
    }
}

window.onclick = function(e) {
    if (!e.target.matches('.n_link')) {
        var dd = document.getElementById("n_links");
        if (dd.classList.contains('show')) {
            dd.classList.remove('show');
        }
    }
}