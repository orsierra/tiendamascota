/*$.validator.addMethod("Termina_por",function(value,element,parametro){
    if (value.endsWith(parametro)){
        return
    }
    return false;
    "Debe terminar por {0},@duocuc.cl"
    })
*/
$("#formulario").validate({
    "rules":{
        "nombre":{
            Required:true,
            minlength:3
        },
        "email":{
            Required:true,
            email:true,
        },
        "numero":{
            Required:true,
            numero:true
        },
        "fecha":{
            Required:true,
        },
        "contraseña":{
            Required:true,
            minlength:5
        },
        "r_contraseña":{
            Required:true,
            minlength:5,
            equalTo:"#contraseña"
        }
    },message:{
        "nombre":{
            Required:'Es obligatorio el dato',
            minlength:'Minimo 3 carateres'
        },
        "email":{
            Required:'Es obligatorio el dato',
            email:'Imail que se pueda validar en caso de necesitar recuperar contraseña',
        },
        "numero":{
            Required:'Es obligatorio el dato',
            numero:'Solo permite numeros este campos'
        },
        "fecha":{
            Required:'Es obligatorio el dato'
        },
        "contraseña":{
            Required:'Es obligatorio el dato',
            minlength:'Minimo 5 caracteres' 
        },
        "r_contraseña":{
            Required:'Es obligatorio el dato',
            minlength:'Minimo 5 caracteres',
            equalTo:'La contraseña debe ser similares'
        }
    }
})
$("#guardar").click(function(){
    let nombre=$("#nombre").value()
    let email=$("#nombre").value()
    let numero=$("#numero").value()
    let fecha=$("#fecha").value()
    let contraseña=$("#contraseña").value()
    let r_contraseña=$("#r_contraseña").value()
})
/*
$("#email").rules("add", { Termina_por: true });
*/  