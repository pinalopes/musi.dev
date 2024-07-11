function contar(){
    let inicio=document.getElementById('comecon')
    let fim=document.getElementById('fimn')
    let passo=document.getElementById('pasn')
    let res=document.getElementById('res')
    
    if (inicio.value.length==0 || fim.value.length==0 || passo.value.length==0){
        res.innerText='Impossível contar'
    }else{
        res.innerHTML='Contando:<br>'
        let i=Number(inicio.value)
        let f=Number(fim.value)
        let p=Number(passo.value)
        if (p<=0){
            window.alert('Passo inválido! Considerando passo 1')
            p=1
        }
        if(i<f){
            for(let c=i ; c<=f ; c += p ){//sempre necessário o contador em todas as ocasiões
             res.innerHTML+= ` ${c} \u{1F449}`
        }
        res.innerHTML+=`\u{1F3C1}` 
        }else{
            for(let c=i; c>=f; c-=p){
                res.innerHTML+=` ${c} \u{1F449}`
            }
        res.innerHTML+=`\u{1F3C1}`  
        }
       
    }
}