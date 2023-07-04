function validarSoloTexto(id_campo,id_alerta){
    esTexto = /[a-z].+[A-Z]/;
    elCampo = document.getElementById(id_campo);
    valorDelCampo = document.getElementById(id_campo).value;
    parrafoAlerta = document.getElementById(id_alerta)
    if(valorDelCampo.lenght==0){
        elCampo.focus();
        elCampo.style.borderColor = "red";
        parrafoAlerta.innerHTML="* Debe ser completado";
        parrafoAlerta.style.color="red";
        
    }else if(!esTexto.test(valorDelCampo)){
        elCampo.focus();
        elCampo.style.borderColor = "red";
        parrafoAlerta.innerHTML="* Solo se admiten letras";
        parrafoAlerta.style.color="red";
        
    }

}
function validarEmail(id_campo,id_alerta){
    esMail = /\w+@\w+\.+[a-z]/;
    elCampo = document.getElementById(id_campo);
    valorDelCampo = document.getElementById(id_campo).value;
    parrafoAlerta = document.getElementById(id_alerta)
    if(valorDelCampo.lenght==0){
        elCampo.focus();
        elCampo.style.borderColor = "red";
        parrafoAlerta.innerHTML="* Debe ser completado";
        parrafoAlerta.style.color="red";
        
    }else if(!esMail.test(valorDelCampo)){
        elCampo.focus();
        elCampo.style.borderColor = "red";
        parrafoAlerta.innerHTML="* Solo se admiten letras";
        parrafoAlerta.style.color="red";
        
    }

}
//se usa con variable con comprobador . test( campo a verificar);
esMail = /\w+@\w+\.+[a-z]/;
esTexto = /[a-z]+[A-Z]/;
//se una con campo . match( variable con comprobador);
esContra =  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
