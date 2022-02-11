


$(document).ready(function(){
    anime({
        targets: '.modal',
        translateY: 50
    });
    
    //startanimate();
    
   
    $('#elminarModal').modal({backdrop: 'static', keyboard: false});
    $('#elminarModal').modal('show')
    $('#mdllogout').modal('show')
    $( "#fondop" ).load("/Persona/loadPersona");
    $( "#fondor" ).load("/Rol/loadrol");
    $( "#fondou" ).load("/Usuario/loadusuario");
    $( "#fondotc" ).load("/Tiposcasos/tiposcaso");
    $( "#fondoc" ).load("/Caso/loadcaso");
    $('#id_Caso').hide()
    $('#id_usuario').hide()
    document.getElementById('id_usuario').value =sessionStorage['idusuario'];
    document.getElementById('id_Caso').value =sessionStorage['idcaso'];
    $("label[for='id_usuario']").hide()
    
    $("label[for='id_Caso']").hide()
    $(function () {
        $('[data-toggle="popover"]').popover()
        })
    //finshanimate();                   
    });
function Animation(runM){
    anime({
        targets: '.modal',
        translateY: runM
    });
  
    
    }

function startanimate(){
    anime({
    targets: '.container-fluid',
    translateX: 100,
     direction: 'reverse',
      
    });
    }
  
(function($) {
    

    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });
})(jQuery);



