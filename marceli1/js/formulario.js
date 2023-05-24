var inputs = document.getElementsByClassName('formulario__input');
for (var i = 0; i < inputs.length; i++) {
  inputs[i].addEventListener('keyup', function(){
    if(this.value.length>=1) {
      this.nextElementSibling.classList.add('fijar')
    } else {
      this.nextElementSibling.classList.remove('fijar')
    }
  });
}

const $formContacto = document.querySelector(formulario)
$formContacto.addEventListener('submint', submitManual())
async function submitManual(event){
  event.preventDefault()
  const form = new FormData(this)
  const respuesta =  await fetch(this.action, {
    method:'post',
    body: form,
    headers:{
      'Accept': 'applicatio/json'
      }
  }) 
  if (Response.ok){
    this.reset()
    alert("gracias por contactarnos")
  }
}