var cod=0;
var total=0;

function check_my_coins(){
  var per=document.getElementById("persona");
  cod=parseInt(per.options[per.selectedIndex].value);
  var coins = 15;
  if (cod==213){// anotar ruts con bonus
    coins += 5;
  }
  if (cod==0){
    coins =0;
  }
  document.getElementById("my-coins").innerHTML=coins;
  return coins;
}

function check_comp(){
  var c=0;
  //Alumnos taller de computación
  var c01 = document.getElementById('c01');
  c = c +  parseInt(c01.options[c01.selectedIndex].value);
  var c02 = document.getElementById('c02');
  c = c +  parseInt(c02.options[c02.selectedIndex].value);
  var c03 = document.getElementById('c03');
  c = c +  parseInt(c03.options[c03.selectedIndex].value);
  var c04 = document.getElementById('c04');
  c = c +  parseInt(c04.options[c04.selectedIndex].value);
  var c05 = document.getElementById('c05');
  c = c +  parseInt(c05.options[c05.selectedIndex].value);
  var c06 = document.getElementById('c06');
  c = c +  parseInt(c06.options[c06.selectedIndex].value);
  var c07 = document.getElementById('c07');
  c = c +  parseInt(c07.options[c07.selectedIndex].value);
  var c08 = document.getElementById('c08');
  c = c +  parseInt(c08.options[c08.selectedIndex].value);
  var c09 = document.getElementById('c09');
  c = c +  parseInt(c09.options[c09.selectedIndex].value);
  var c10 = document.getElementById('c10');
  c = c +  parseInt(c10.options[c10.selectedIndex].value);
  var c11 = document.getElementById('c11');
  c = c +  parseInt(c11.options[c11.selectedIndex].value);
  var c12 = document.getElementById('c12');
  c = c +  parseInt(c12.options[c12.selectedIndex].value);
  var c13 = document.getElementById('c13');
  c = c +  parseInt(c13.options[c13.selectedIndex].value);


  if (((cod>=300)) && (c != 0)){
    document.getElementById('warning-comp').style.display="block";
    return 0;
  }

  return c;
}

function check_dis(){
  var d=0;
  //Alumnos taller de diseño
  var d01 = document.getElementById('d01');
  d = d +  parseInt(d01.options[d01.selectedIndex].value);
  var d02 = document.getElementById('d02');
  d = d +  parseInt(d02.options[d02.selectedIndex].value);
  var d03 = document.getElementById('d03');
  d = d +  parseInt(d03.options[d03.selectedIndex].value);
  var d04 = document.getElementById('d04');
  d = d +  parseInt(d04.options[d04.selectedIndex].value);
  var d05 = document.getElementById('d05');
  d = d +  parseInt(d05.options[d05.selectedIndex].value);
  var d06 = document.getElementById('d06');
  d = d +  parseInt(d06.options[d06.selectedIndex].value);
  var d07 = document.getElementById('d07');
  d = d +  parseInt(d07.options[d07.selectedIndex].value);
  var d08 = document.getElementById('d08');
  d = d +  parseInt(d08.options[d08.selectedIndex].value);
  var d09 = document.getElementById('d09');
  d = d +  parseInt(d09.options[d09.selectedIndex].value);
  var d10 = document.getElementById('d10');
  d = d +  parseInt(d10.options[d10.selectedIndex].value);
  var d11 = document.getElementById('d11');
  d = d +  parseInt(d11.options[d11.selectedIndex].value);
  var d12 = document.getElementById('d12');
  d = d +  parseInt(d12.options[d12.selectedIndex].value);
  var d13 = document.getElementById('d13');
  d = d +  parseInt(d13.options[d13.selectedIndex].value);
  var d14 = document.getElementById('d14');
  d = d +  parseInt(d14.options[d14.selectedIndex].value);
  var d15 = document.getElementById('d15');
  d = d +  parseInt(d15.options[d15.selectedIndex].value);

  if ((cod>=100 && cod<=200) && (d != 0)){
    document.getElementById('warning-dis').style.display="block";
    return 0;
  }

  return d;
}

function check_model(){
  var m=0;
  //Alumnos taller de modelo digital
  var m01 = document.getElementById('m01');
  m = m +  parseInt(m01.options[m01.selectedIndex].value);
  var m02 = document.getElementById('m02');
  m = m +  parseInt(m02.options[m02.selectedIndex].value);
  var m03 = document.getElementById('m03');
  m = m +  parseInt(m03.options[m03.selectedIndex].value);
  var m04 = document.getElementById('m04');
  m = m +  parseInt(m04.options[m04.selectedIndex].value);
  var m05 = document.getElementById('m05');
  m = m +  parseInt(m05.options[m05.selectedIndex].value);
  var m06 = document.getElementById('m06');
  m = m +  parseInt(m06.options[m06.selectedIndex].value);
  var m07 = document.getElementById('m07');
  m = m +  parseInt(m07.options[m07.selectedIndex].value);
  var m08 = document.getElementById('m08');
  m = m +  parseInt(m08.options[m08.selectedIndex].value);
  var m09 = document.getElementById('m09');
  m = m +  parseInt(m09.options[m09.selectedIndex].value);
  var m10 = document.getElementById('m10');
  m = m +  parseInt(m10.options[m10.selectedIndex].value);
  var m11 = document.getElementById('m11');
  m = m +  parseInt(m11.options[m11.selectedIndex].value);
  var m12 = document.getElementById('m12');
  m = m +  parseInt(m12.options[m12.selectedIndex].value);
  var m13 = document.getElementById('m13');
  m = m +  parseInt(m13.options[m13.selectedIndex].value);

  if ((cod>=200 && cod<=300) && (m != 0)){
    document.getElementById('warning-model').style.display="block";
    return 0;
  }

  return m;
}

function check_sale(){
  total=0;
  clean();
  var btcoins= check_my_coins();
  var rst= btcoins - check_dis() - check_model() - check_comp() ;
  if (rst >= 0) {
    //mostrar el resto
    document.getElementById('resto-bueno').innerHTML= rst;
    document.getElementById('final-bueno').style.display="block";
  } else {
    document.getElementById('final-error').style.display="block";
  }

}

function clean(){
  document.getElementById('warning-comp').style.display="none";
  document.getElementById('warning-dis').style.display="none";
  document.getElementById('warning-model').style.display="none";
  document.getElementById('final-error').style.display="none";
  document.getElementById('final-bueno').style.display="none";
}
