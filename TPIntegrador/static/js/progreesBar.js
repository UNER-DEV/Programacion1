const randomColor = "#"+((1<<24)*Math.random()|0).toString(16); 
document.documentElement.style.setProperty('--color-random', randomColor);

$(function() {
    var min = 0,
        max = 8,
        $step = $("#step"),
        $msg = $("#msg");
  
    function norm(value, min, max) {
      return (value - min) / (max - min);
    }
  
    function lerp(norm, min, max) {
      return (max - min) * norm + min;
    }
  
    function map(value, sourceMin, sourceMax, destMin, destMax) {
      return lerp(norm(value, sourceMin, sourceMax), destMin, destMax);
    }
  
    function isInt(value) {
      return !isNaN(value) && 
             parseInt(Number(value)) == value && 
             !isNaN(parseInt(value, 10));
    }
  
    function refresh() {
      var step = $step.val();
  
      if (step) {
        if (isInt(min) && isInt(max) && isInt(step)) {
          var result = map(step, min, max, 0, 100);
          if (result < 0) {
            $("#bar").text("Invalido");
            $("#de").prop("Desactivado", true).css("opacity", 0.5);
            return;
          } else if (result > 100) {
            $("#bar").text("Invalido");
            $("#in").prop("Desactivado", true).css("opacity", 0.5);
            return;
          } else {
            $("#in, #de").prop("Desactivado", false).css("opacity", 1);
            $("#bar").text("ESCALÓN " + step + " / 8").css('width', result + "%");
          }
          $msg.hide();
        } else {
          $msg.text("Ingrese un numero!!!").show();
        }
      }
    }

    $step.on("input", refresh);    
    refresh();
    
  });