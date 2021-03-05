var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    y = 0;
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(frame, 30);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
        document.getElementById("msg").innerHTML = "ΟΛΟΚΛΗΡΩΣΗ ΘΕΡΜΟΜΕΤΡΗΣΗΣ";
        t=random(352,400)/10;
        if (t<=36.6){
          Swal.fire('ΘΕΡΜΟΚΡΑΣΙΑ: ' + t,'Η ΘΕΡΜΟΚΡΑΣΙΑ ΣΑΣ ΕΙΝΑΙ ΕΝΤΑΞΕΙ ΜΠΟΡΕΙΤΕ ΝΑ ΕΙΣΕΛΘΕΤΕ!','success').then(function() {window.location = "index.html";});
        }else if (t<=37.2){
          Swal.fire('ΘΕΡΜΟΚΡΑΣΙΑ: ' + t,'Η ΘΕΡΜΟΚΡΑΣΙΑ ΣΑΣ ΕΙΝΑΙ ΛΙΓΟ ΑΥΞΗΜΕΝΗ. ΠΑΡΑΚΑΛΩ ΞΕΚΟΥΡΑΣΤΕΙΤΕ 5 ΛΕΠΤΑ ΚΑΙ ΞΑΝΑΘΕΡΜΟΜΕΤΡΗΘΕΙΤΕ!','warning');
          document.getElementById("thermo").style.visibility="visible";
        }else if (t<=38.0){
          Swal.fire('ΘΕΡΜΟΚΡΑΣΙΑ: ' + t,'Η ΘΕΡΜΟΚΡΑΣΙΑ ΣΑΣ ΕΙΝΑΙ ΑΥΞΗΜΕΝΗ. ΔΕΝ ΜΠΟΡΕΙΤΕ ΝΑ ΕΙΣΕΛΘΕΤΕ ΚΑΙ ΑΠΟΧΩΡΕΙΣΤΕ ΜΕ ΠΡΟΣΟΧΗ!','error').then(function() {window.location = "index.html";});
        }else if (t>38.0){
          Swal.fire('ΘΕΡΜΟΚΡΑΣΙΑ: ' + t,'Η ΘΕΡΜΟΚΡΑΣΙΑ ΣΑΣ ΕΙΝΑΙ ΥΨΗΛΗ. ΔΕΝ ΜΠΟΡΕΙΤΕ ΝΑ ΕΙΣΕΛΘΕΤΕ ΚΑΙ ΣΑΣ ΠΡΟΤΕΙΝΟΥΜΕ ΝΑ ΚΑΝΕΤΕ ΤΕΣΤ ΚΟΡΟΝΟΙΟΥ! ΚΟΝΤΙΝΟΤΕΡΟ ΚΕΝΤΡΟ ΥΓΕΙΑΣ: ΝΟΣΟΚΟΜΕΙΟ ΤΖΑΝΕΙΟ.','error').then(function() {window.location = "index.html";});
        }
      } else {
        width++;
        y++;
        if (width%45==0)
        {
          document.getElementById("msg").innerHTML = "ΘΕΡΜΟΜΕΤΡΗΣΗ.";
        }else if (width%45==15) {
          document.getElementById("msg").innerHTML = "ΘΕΡΜΟΜΕΤΡΗΣΗ..";
        }else if (width%45==30){
          document.getElementById("msg").innerHTML = "ΘΕΡΜΟΜΕΤΡΗΣΗ...";
        }
        elem.innerHTML = width  + "%";
        elem.style.width = width + "%";
      }
    }
  }
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
