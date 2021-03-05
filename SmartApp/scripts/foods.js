function update(){
  var tmp=document.getElementsByClassName("plist");
  var f=[];
  var p=[];
  var q=[]
  for(var i = 0; i < tmp.length; i++) {
    if ((i+2)%2==0){
      f.push(tmp[i].innerHTML);
    }else{
      p.push((tmp[i].innerHTML).slice(0,-1));
    }
  }
  q.push(document.getElementById('quant1').value);
  q.push(document.getElementById('quant2').value);
  q.push(document.getElementById('quant3').value);
  q.push(document.getElementById('quant4').value);
  q.push(document.getElementById('quant5').value);
  q.push(document.getElementById('quant6').value);
  q.push(document.getElementById('quant7').value);
  q.push(document.getElementById('quant8').value);
  q.push(document.getElementById('quant9').value);
  q.push(document.getElementById('quant10').value);
  var t=[];
  var price=0;
  for(i in q){
    if (q[i]!=0){
    t.push(q[i]+"X "+f[i]);
    price+=q[i]*p[i];
  }
  }
  document.getElementById('foods').innerHTML=t;
  document.getElementById('price').innerHTML=price+"€";
}

function cont(){

  var price=document.getElementById('price').innerHTML;
  var foods=document.getElementById('foods').innerHTML;
  if (price.slice(0,-1)!=0){
  Swal.fire({
  title: 'ΣΥΝΟΛΟ ΠΑΡΑΓΓΕΛΙΑΣ: '+ price,
  text: "ΠΡΟΙΟΝΤΑ: " + foods,
  icon: 'warning',
  showCancelButton: true,
  cancelButtonText: 'ΑΚΥΡΩΣΗ',
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'ΣΥΝΕΧΕΙΑ ΠΑΡΑΓΓΕΛΙΑΣ'
  }).then((result) => {
  if (result.isConfirmed) {
    window.location.replace("order.html");
  }
})}else{
  Swal.fire(
  '',
  'ΔΕΝ ΕΧΕΤΕ ΕΠΙΛΕΞΕΙ ΚΑΤΙ ΑΠΟ ΤΟ ΜΕΝΟΥ',
  'error'
)
}
}

function cardnumber(inputtxt)
{
  var cardno = /^[0-9]{4}[ ][0-9]{4}[ ][0-9]{4}[ ][0-9]{4}$/;
  if (cardno.test(inputtxt)){
    return true;
  }
  else{
    return false;
  }
}

function nameletter(inputtxt)
{
  var namel= /^[a-zA-Z ]+$/;
  if (namel.test(inputtxt)){
    return true;
  }
  else{
    return false;
  }
}

function date(inputtxt)
{
  var date= /^\d{2}\/\d{2}$/;
  if (date.test(inputtxt)){
    return true;
  }
  else{
    return false;
  }
}

function cvvtest(inputtxt)
{
  var cvv= /^[0-9]{3}$/;
  if (cvv.test(inputtxt)){
    return true;
  }
  else{
    return false;
  }
}

function pay(){
  var a=document.getElementById('cno').value;
  var b=document.getElementById('name').value;
  var c=document.getElementById('exp').value;
  var d=document.getElementById('cvv').value;
  console.log(cardnumber(a));
  if(cardnumber(a) && a!="" && nameletter(b) && b!="" && c!="" && date(c) && d!="" && cvvtest(d)){
  Swal.fire(
  'ΕΠΙΤΥΧΙΑ ΠΑΡΑΓΓΕΛΙΑΣ',
  'Η ΠΑΡΑΓΓΕΛΙΑ ΣΑΣ ΟΛΟΚΛΗΡΩΘΗΚΕ ΕΠΙΤΥΧΩΣ. ΚΑΛΗ ΣΑΣ ΟΡΕΞΗ!',
  'success').then(function() {window.location.replace("index.html");});
}else if (cardnumber(a)==false || a=="") {
  Swal.fire(
  'ΣΦΑΛΜΑ',
  'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤON ΑΡΙΘΜΟ ΚΑΡΤΑΣ',
  'error')
}else if (nameletter(b)==false || b=="") {
  Swal.fire(
  'ΣΦΑΛΜΑ',
  'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤO ΟΝΟΜΑ ΚΑΤΟΧΟΥ',
  'error')
}else if (date(c)==false || c=="") {
  Swal.fire(
  'ΣΦΑΛΜΑ',
  'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤΗΝ ΗΜ.ΛΗΞΗΣ',
  'error')
}else if (cvvtest(d)==false || d=="") {
  Swal.fire(
  'ΣΦΑΛΜΑ',
  'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤO CVV',
  'error')
}
else{
  Swal.fire(
  'ΣΦΑΛΜΑ',
  'ΣΥΜΠΛΗΡΩΣΤΕ ΣΩΣΤΑ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ',
  'error'
)
}
}
