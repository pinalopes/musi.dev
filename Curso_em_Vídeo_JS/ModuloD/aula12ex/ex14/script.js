function carregar(){
    var msg=document.getElementById('msg')
    var img=document.getElementById('imagem')
    var data= new Date()
    var hora=data.getHours()
    var min=data.getMinutes()
    msg.innerHTML=`Agora são ${hora} horas e ${min} minutos`   
    if (hora>=0 && hora <12){
        img.src='fotomanha.png'
        document.body.style.background='#333d25'//sempre que for copiar uma cor de algum outro local, não esquecer de colocar a # na frente
    }else if (hora>=12 && hora<=18){
        img.src='fototarde.png'
          document.body.style.background='#ffad0b'
    }else{
        img.src='fotonoite.png'
          document.body.style.background='#14263f'
    }
}

