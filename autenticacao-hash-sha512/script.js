const nome = document.getElementById("nome");
const senha = document.getElementById("senha");

document.getElementById ("btn_entrar").addEventListener ("click",function(){
localStorage.setItem("nome", nome.value)
let senha_criptografada= CryptoJS.SHA512(senha.value).toString()
localStorage.setItem("senha" ,senha_criptografada)
})

let a = localStorage.getItem("nome")
let b = localStorage.getItem("senha")


console.log (a)
console.log (b)






















