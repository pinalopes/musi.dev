var idade=77
console.log(`Você tem ${idade} anos`)
if(idade<16){
    console.log(`Não vota`)
}else if(idade<18 || idade>65){//coloca se o else if junto para ocupar menos espaço e o && é o mesmo que o and do python e o || tem sentido de or
    console.log('Voto opcional')
}else{
    console.log('Voto obrigatório')
}