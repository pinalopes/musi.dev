function clique(){
    var data=new Date()
    var ano=data.getFullYear()
    var fnasc=document.getElementById('txtano')
    var res=document.getElementById('res')
    if (fnasc.value.length==0 || fnasc.value>ano){
        alert('[ERRO] Verifique os dados e tente novamente')
    }else{
        var fsex=document.getElementsByName('radsex')
        var idade= ano-Number(fnasc.value)
        res.innerHTML=`Idade calculada ${idade}`
        var genero=''
        var img=document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked){
            genero='Homem'
            if (idade>=0 && idade<=10){
                img.setAttribute('src','bebe_m.png')
            }else if(idade<21){
                img.setAttribute('src','jovem_m.png')
            }else if(idade <50) {
                img.setAttribute('src','adulto_m.png')
            }else{
                img.setAttribute('src','idoso_m.png')
            }
        }else{
            genero='Mulher'
            if (idade>=0 && idade<10){
                img.setAttribute('src','bebe_f.png')
            }else if(idade<21){
                img.setAttribute('src','jovem_f.png')
            }else if(idade <50) {
                img.setAttribute('src','adulta_f.png')
            }else{
                img.setAttribute('src','idosa_f.png')
            }
        }
        res.style.textAlign='center'
        res.innerHTML=`Detectamos ${genero} com ${idade} anos`
        res.appendChild(img)
    }
}