function onHandleClick(elemento){
    let buttons = $('.btnQuestionCheck');
    for(let i =0; i<buttons.length;i++){
        buttons[i].classList.remove('active');
    }
        elemento.classList.add('active');
}