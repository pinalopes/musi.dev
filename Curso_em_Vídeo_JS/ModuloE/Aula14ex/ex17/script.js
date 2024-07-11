function clicar(){
    var numero=document.getElementById('txtn')
    var res=document.getElementById('txts')

    if (numero.value.length==0){
        alert('Por favor Digite um número! ')
    }else{
        let n=Number(numero.value)
        res.innerHTML=''
        for(let c=1;c<=10;c++){
            let item=document.createElement('option')
            item.text= `${n} X ${c} = ${n*c}`
            item.value=`tab${c}`
            res.appendChild(item)
            
        }
    }
}