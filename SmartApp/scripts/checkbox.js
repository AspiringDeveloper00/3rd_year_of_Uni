function doalert1(a1) {

  var a1=document.getElementById("myonoffswitch1");
  if (a1.checked) {
    document.getElementById("a1").style.backgroundColor = "#62a3d2";
  } else {
    document.getElementById("a1").style.backgroundColor = "#30475e";
  }
}

function doalert2() {
  var a2=document.getElementById("myonoffswitch2");
  if (a2.checked) {
    document.getElementById("a2").style.backgroundColor = "#62a3d2";
  } else {
    document.getElementById("a2").style.backgroundColor = "#30475e";
  }

}
function doalert3() {
    var a3=document.getElementById("myonoffswitch3");
    if (a3.checked) {
      document.getElementById("a3").style.backgroundColor = "#62a3d2";
    } else {
      document.getElementById("a3").style.backgroundColor = "#30475e";
    }
}
function doalert4() {
    var a4=document.getElementById("myonoffswitch4");
    if (a4.checked) {
      document.getElementById("a4").style.backgroundColor = "#62a3d2";
    } else {
      document.getElementById("a4").style.backgroundColor = "#30475e";
    }

}
function doalert5() {
  var a5=document.getElementById("myonoffswitch5");
  if (a5.checked) {
    document.getElementById("a5").style.backgroundColor = "#62a3d2";
  } else {
    document.getElementById("a5").style.backgroundColor = "#30475e";
  }

}
function doalert6() {
  var a6=document.getElementById("myonoffswitch6");
  if (a6.checked) {
    document.getElementById("a6").style.backgroundColor = "#62a3d2";
  } else {
    document.getElementById("a6").style.backgroundColor = "#30475e";
  }
}

function check(){
  doalert1();
  doalert2();
  doalert3();
  doalert4();
  doalert5();
  doalert6();
}

function startbath(){
  document.getElementById("myonoffswitch1").checked= JSON.parse(sessionStorage.getItem('bath1'));
  document.getElementById("myonoffswitch2").checked= JSON.parse(sessionStorage.getItem('bath2'));
  document.getElementById("myonoffswitch3").checked= JSON.parse(sessionStorage.getItem('bath3'));
  document.getElementById("myonoffswitch4").checked= JSON.parse(sessionStorage.getItem('bath4'));
  document.getElementById("myonoffswitch5").checked= JSON.parse(sessionStorage.getItem('bath5'));
  document.getElementById("myonoffswitch6").checked= JSON.parse(sessionStorage.getItem('bath6'));
  check();
}

function startbed(){
  document.getElementById("myonoffswitch1").checked= JSON.parse(sessionStorage.getItem('bed1'));
  document.getElementById("myonoffswitch2").checked= JSON.parse(sessionStorage.getItem('bed2'));
  document.getElementById("myonoffswitch3").checked= JSON.parse(sessionStorage.getItem('bed3'));
  document.getElementById("myonoffswitch4").checked= JSON.parse(sessionStorage.getItem('bed4'));
  document.getElementById("myonoffswitch5").checked= JSON.parse(sessionStorage.getItem('bed5'));
  document.getElementById("myonoffswitch6").checked= JSON.parse(sessionStorage.getItem('bed6'));
  check();
}

function startkitch(){
  document.getElementById("myonoffswitch1").checked= JSON.parse(sessionStorage.getItem('kitch1'));
  document.getElementById("myonoffswitch2").checked= JSON.parse(sessionStorage.getItem('kitch2'));
  document.getElementById("myonoffswitch3").checked= JSON.parse(sessionStorage.getItem('kitch3'));
  document.getElementById("myonoffswitch4").checked= JSON.parse(sessionStorage.getItem('kitch4'));
  document.getElementById("myonoffswitch5").checked= JSON.parse(sessionStorage.getItem('kitch5'));
  document.getElementById("myonoffswitch6").checked= JSON.parse(sessionStorage.getItem('kitch6'));
  check();
}

function startliv(){
  document.getElementById("myonoffswitch1").checked= JSON.parse(sessionStorage.getItem('liv1'));
  document.getElementById("myonoffswitch2").checked= JSON.parse(sessionStorage.getItem('liv2'));
  document.getElementById("myonoffswitch3").checked= JSON.parse(sessionStorage.getItem('liv3'));
  document.getElementById("myonoffswitch4").checked= JSON.parse(sessionStorage.getItem('liv4'));
  document.getElementById("myonoffswitch5").checked= JSON.parse(sessionStorage.getItem('liv5'));
  document.getElementById("myonoffswitch6").checked= JSON.parse(sessionStorage.getItem('liv6'));
  check();
}
