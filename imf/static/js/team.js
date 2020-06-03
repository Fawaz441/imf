var member_info = document.querySelectorAll('.mem_faded');

function wave(){
    for(var x=0;x<member_info.length;x++){
        var appearHeight = window.innerHeight / 0.9;
        var self_height = member_info[x].getBoundingClientRect().top;
        if(self_height < appearHeight){
            member_info[x].style.opacity = 1;
            member_info[x].style.transform ='translateY(0)'; 
        }
    }
}

if(window.innerWidth<=500){
window.addEventListener('scroll',wave);
}