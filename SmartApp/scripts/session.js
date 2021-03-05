function startses(){

  sessionStorage.setItem('name', document.getElementById('name').value);

  sessionStorage.setItem('bath1', false);
  sessionStorage.setItem('bath2', false);
  sessionStorage.setItem('bath3', false);
  sessionStorage.setItem('bath4', false);
  sessionStorage.setItem('bath5', false);
  sessionStorage.setItem('bath6', false);

  sessionStorage.setItem('bed1', false);
  sessionStorage.setItem('bed2', false);
  sessionStorage.setItem('bed3', false);
  sessionStorage.setItem('bed4', false);
  sessionStorage.setItem('bed5', false);
  sessionStorage.setItem('bed6', false);

  sessionStorage.setItem('kitch1', false);
  sessionStorage.setItem('kitch2', false);
  sessionStorage.setItem('kitch3', false);
  sessionStorage.setItem('kitch4', false);
  sessionStorage.setItem('kitch5', false);
  sessionStorage.setItem('kitch6', false);

  sessionStorage.setItem('liv1', false);
  sessionStorage.setItem('liv2', false);
  sessionStorage.setItem('liv3', false);
  sessionStorage.setItem('liv4', false);
  sessionStorage.setItem('liv5', false);
  sessionStorage.setItem('liv6', false);

  sessionStorage.setItem('plan', "null")

}

function savebath(){
  sessionStorage.setItem('bath1', document.getElementById("myonoffswitch1").checked);
  sessionStorage.setItem('bath2', document.getElementById("myonoffswitch2").checked);
  sessionStorage.setItem('bath3', document.getElementById("myonoffswitch3").checked);
  sessionStorage.setItem('bath4', document.getElementById("myonoffswitch4").checked);
  sessionStorage.setItem('bath5', document.getElementById("myonoffswitch5").checked);
  sessionStorage.setItem('bath6', document.getElementById("myonoffswitch6").checked);
  location.href="control.html";
}

function savebed(){
  sessionStorage.setItem('bed1', document.getElementById("myonoffswitch1").checked);
  sessionStorage.setItem('bed2', document.getElementById("myonoffswitch2").checked);
  sessionStorage.setItem('bed3', document.getElementById("myonoffswitch3").checked);
  sessionStorage.setItem('bed4', document.getElementById("myonoffswitch4").checked);
  sessionStorage.setItem('bed5', document.getElementById("myonoffswitch5").checked);
  sessionStorage.setItem('bed6', document.getElementById("myonoffswitch6").checked);
  location.href="control.html";
}
function savekitch(){
  sessionStorage.setItem('kitch1', document.getElementById("myonoffswitch1").checked);
  sessionStorage.setItem('kitch2', document.getElementById("myonoffswitch2").checked);
  sessionStorage.setItem('kitch3', document.getElementById("myonoffswitch3").checked);
  sessionStorage.setItem('kitch4', document.getElementById("myonoffswitch4").checked);
  sessionStorage.setItem('kitch5', document.getElementById("myonoffswitch5").checked);
  sessionStorage.setItem('kitch6', document.getElementById("myonoffswitch6").checked);
  location.href="control.html";
}
function saveliv(){
  sessionStorage.setItem('liv1', document.getElementById("myonoffswitch1").checked);
  sessionStorage.setItem('liv2', document.getElementById("myonoffswitch2").checked);
  sessionStorage.setItem('liv3', document.getElementById("myonoffswitch3").checked);
  sessionStorage.setItem('liv4', document.getElementById("myonoffswitch4").checked);
  sessionStorage.setItem('liv5', document.getElementById("myonoffswitch5").checked);
  sessionStorage.setItem('liv6', document.getElementById("myonoffswitch6").checked);
  location.href="control.html";
}

function logout(){
  sessionStorage.clear();
  location.replace("login.html");
}


function sms(msg){
  sessionStorage.setItem('msg', msg);
  location.href="plaisio.html";
}

function validateTime(time) {
  const timeReg = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;
  return timeReg.test(time);
}

function saveplan(){
  var msg=sessionStorage.getItem('msg');
  var time=document.getElementById("time").value;
  var t=document.getElementById("transport");
  var transport=t.options[t.selectedIndex].text;
  if (document.getElementById("yes").checked){
    coffee="ΝΑΙ";
  }else if (document.getElementById("no").checked){
    coffee="ΟΧΙ";
  }else{
    coffee="false";
  }

  if(validateTime(time) && transport!="-- select an option --" && coffee!="false"){


    if (msg=="ΦΑΡΜΑΚΕΙΟ/ΓΙΑΤΡΟΣ"){
      if(transport=="Πεζός/Ποδήλατο"){
        route="Images/fp.png";
      }else if(transport=="Μέσα Μαζικής Μεταφοράς"){
        route="Images/fm.png";
      }else{
        route="Images/fa.png";
      }
    }else if(msg=="ΣΟΥΠΕΡΜΑΡΚΕΤ"){
      if(transport=="Πεζός/Ποδήλατο"){
        route="Images/sp.png";
      }else if(transport=="Μέσα Μαζικής Μεταφοράς"){
        route="Images/sm.png";
      }else{
        route="Images/sa.png";
      }
    }else if(msg=="ΤΡΑΠΕΖΑ"){
      if(transport=="Πεζός/Ποδήλατο"){
        route="Images/tp.png";
      }else if(transport=="Μέσα Μαζικής Μεταφοράς"){
        route="Images/tp.png";
      }else{
        route="Images/ta.png";
      }
    }else if (msg=="ΕΡΓΑΣΙΑ"){
      if(transport=="Πεζός/Ποδήλατο"){
        route="Images/ep.png";
      }else if(transport=="Μέσα Μαζικής Μεταφοράς"){
        route="Images/em.png";
      }else{
        route="Images/ea.png";
      }
    }else if (msg=="ΚΗΔΕΙΑ"){
      route="";
    }else if (msg=="ΑΤΟΜΙΚΗ ΑΘΛΗΣΗ"){
      route="";
    }else if (msg=="ΠΑΡΟΧΗ ΒΟΗΘΕΙΑΣ"){
      route="";
    }

    if (coffee=="ΝΑΙ"){
      coffee="ZAMBRI, Αγίου Δημητρίου 9";
    }else{
      coffee="-"
    }

    if (sessionStorage.getItem('plan') == "null"){
      array=[[msg,time,transport,coffee,route]];
      sessionStorage.setItem('plan', JSON.stringify(array));
      Swal.fire(
        'ΕΠΙΤΥΧΙΑ',
        'Η ΜΕΤΑΚΙΝΗΣΗ ΠΡΟΣΤΕΘΗΚΕ ΣΤΟ ΠΛΑΝΟ ΗΜΕΡΑΣ',
        'success').then(function() {window.location = "smsplan.html";});
    }else{
      array=JSON.parse(sessionStorage.getItem('plan'));
      array.push([msg,time,transport,coffee,route]);
      sessionStorage.setItem('plan', JSON.stringify(array));
      Swal.fire(
        'ΕΠΙΤΥΧΙΑ',
        'Η ΜΕΤΑΚΙΝΗΣΗ ΠΡΟΣΤΕΘΗΚΕ ΣΤΟ ΠΛΑΝΟ ΗΜΕΡΑΣ',
        'success').then(function() {window.location = "smsplan.html";});
    }
  }
  else{
    Swal.fire(
    'ΣΦΑΛΜΑ',
    'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ',
    'error'
  )
  }
}


function fall(){

  Swal.fire({
  title: 'ΠΑΡΑΤΗΡΗΘΗΚΕ ΠΤΩΣΗ',
  text: "ΕΙΣΤΕ ΚΑΛΑ; ΧΡΕΙΑΖΕΣΤΕ ΒΟΗΘΕΙΑ;",
  icon: 'warning',
  showCancelButton: true,
  cancelButtonText: 'ΝΑΙ ΕΙΜΑΙ ΚΑΛΑ',
  confirmButtonColor: '#d33',
  cancelButtonColor: '#3085d6',
  confirmButtonText: 'ΘΕΛΩ ΒΟΗΘΕΙΑ'

}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'ΕΡΧΕΤΑΙ ΒΟΗΘΕΙΑ!',
      'ΕΙΔΟΠΟΙΗΘΗΚΑΝ ΟΙ ΥΠΗΡΕΣΙΕΣ ΤΟΥ ΔΗΜΟΥ. ΣΕ ΛΙΓΑ ΛΕΠΤΑ ΘΑ ΕΙΝΑΙ ΚΟΝΤΑ ΣΑΣ.',
      'warning'
    )
  }else{
    Swal.fire(
      'ΕΛΠΙΖΟΥΜΕ ΝΑ ΕΙΣΤΕ ΚΑΛΑ',
      'ΚΑΛΗ ΣΑΣ ΑΝΑΡΡΩΣΗ, ΓΙΑ ΟΤΙΔΗΠΟΤΕ ΧΡΕΙΑΣΤΕΙΤΕ ΕΠΙΚΟΙΝΩΝΕΙΣΤΕ ΜΕ ΤΟΝ ΔΗΜΟ ΜΕ ΤΗ ΧΡΗΣΗ ΤΩΝ ΠΑΡΑΚΑΤΩ ΚΟΥΜΠΙΩΝ.',
      'success'
    )
  }
})

}

function del(j){
  array=JSON.parse(sessionStorage.getItem('plan'));
  for (var i = 0; i <= array.length; i++){
    if (j==i){
      array.splice(j, 1);
    }
  }
  sessionStorage.setItem('plan', JSON.stringify(array));
  Swal.fire({
  title: 'ΔΙΑΓΡΑΦΗ ΜΕΤΑΚΙΝΗΣΗΣ;',
  text: "ΑΥΤΗ Η ΔΙΑΓΡΑΦΗ ΕΙΝΑΙ ΟΡΙΣΤΙΚΗ. ΕΙΣΤΕ ΣΙΓΟΥΡΟΣ;",
  icon: 'warning',
  showCancelButton: true,
  cancelButtonText: "ΑΚΥΡΩΣΗ",
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'ΔΙΑΓΡΑΦΗ'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'ΔΙΑΓΡΑΦΗ',
      'Η ΔΙΑΓΡΑΦΗ ΕΓΙΝΕ ΕΠΙΤΥΧΩΣ',
      'success'
    ).then(function() {window.location = "plan.html";});
  }
})

}

function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}
