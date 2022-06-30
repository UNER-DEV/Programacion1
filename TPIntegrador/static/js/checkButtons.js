$(function() {
  $( document ).ready(function() {
    $('#modalAdd').modal('toggle');
    $('#modalQ').modal('toggle');
    });
});


function onHandleClick(elemento) {
  let buttons = $(".btnQuestionCheck");
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].style.background = "var(--color-font-3)";
  }
  elemento.style.background = "var(--color-btn-3)";
}



