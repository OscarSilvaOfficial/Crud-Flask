$('#create-game').validate({
    rules: {
        nome: {
            required: true
        },
        categoria: {
            required: true
        },
        console: {
            required: true
        }
    },
    messages:{
             nome:{
                    required:"Por favor, informe seu nome",
             },
             categoria:{
                    required:"É necessário informar a categoria"
             },
             console:{
                    required:"A mensagem não pode ficar em branco"
             }     
       }

});