const usuario_login = document.getElementById("login_usuario");
const senha_login = document.getElementById("login_senha");
src = "cadastro.js"



function nome_funcao(){

    window.location.href = 'tela_inicial.html'
}

let a = 0
const senha_cadastrada_no_local_storage = localStorage.getItem("senha")

document.getElementById("btn_entrar_login").addEventListener("click" , function(){
    let senha_criptografada_login = CryptoJS.SHA512(senha_login.value).toString()   
    if (senha_criptografada_login.value == senha_cadastrada_no_local_storage.value){
        a = 1
        nome_funcao()
        
    }
    else{
        console.log("senha invalida")
        
    }
    if(window.location.href == 'tela_inicial.html' && a==0){
        console.log ("deu errado")
    }
}
)

























