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

function populateGame(...args) {

     const id = args[0]
     const jogo = args[1]
     const categoria = args[2]
     const console = args[3]
     
     $('#nome').val(jogo)
     $('#categoria').val(categoria)
     $('#console').val(console)
     $('#modalTitulo').append(`Alterar ${jogo}`)
     $('#id').attr('value', `${id}`)
};

$('#formEdit').submit(function(event) {

    var formData = {
        id: $('#id').val(),
        nome: $('#nome').val(),
        categoria: $('#categoria').val(),
        console: $('#console').val()
    };

    $.ajax({
        type        : 'POST',
        url         : '/editar',
        data        : formData,
        success: function(response) {
            window.location.href ='/'
            //console.log(formData)
        }       
    })

    event.preventDefault();
});

     