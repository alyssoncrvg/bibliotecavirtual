function numero(input){
    var num = /[^0-9]/gi;
    input.value = input.value.replace(num,"");
}

document.body.addEventListener('htmx:configRequest', (event) =>{
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}'
})