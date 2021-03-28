var add_emo = "";
for (var i = 128512; i < 128592; i++) {
add_emo += '<button onclick="pick_emoji('+i+')" id="'+i+'">&#'+i+'; </button>'; 
}
document.getElementById("emobox").innerHTML = add_emo;

var xx = document.getElementById('m-b-1');
function pick_emoji(em_num)
{	var num = em_num.toString();
    num = num.replace(' ','');
    var x = document.getElementById(num);
    xx.value += x.innerHTML;
}
function em_box_show()
{
    document.getElementById("emobox").classList.toggle("show");
}

// window.onclick = function(event) 
// {
//     if (!event.target.matches('.em-btn')) 
//     {
//         var dd1 = document.getElementsByClassName("emo-box");
//         var i;
//         for (i = 0; i < dd1.length; i++) 
//         {
//             var opendd1 = dd1[i];
//             if (opendd1.classList.contains('show')) 
//             {
//                 opendd1.classList.remove('show');
//             }
//         }
//     }
// }