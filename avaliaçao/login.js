const usuario_login = document.getElementById("login_usuario");
const senha_login = document.getElementById("login_senha");






const senha_cadastrada_no_local_storage = localStorage.getItem("senha")

document.getElementById("btn_entrar_login").addEventListener("click" , function(){
    let senha_criptografada_login = CryptoJS.SHA512(senha_login.value).toString()   
    
    if (senha_criptografada_login.value == senha_cadastrada_no_local_storage.value){
        
        window.location.href = 'tela_inicial.html'
        
    }
    else{
        console.log("senha invalida")
        
    }
}
)
















