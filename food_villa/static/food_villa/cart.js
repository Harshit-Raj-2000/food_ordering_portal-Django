validationAlert = document.querySelector('#topAlert')

document.querySelector('.placeOrder').onclick = (e)=>{
    e.preventDefault()
    address = document.querySelector('#address')
    if (address.value == ""){
        validationAlert.innerHTML = "The address field is empty!"
        validationAlert.style.display = "block"
        setTimeout(()=>{
            validationAlert.style.display = "None"
        },4000)
        return
    }

    url = e.target.dataset.url
    csrf = e.target.dataset.csrf
    total = e.target.dataset.total
    data = JSON.stringify({
        address: address.value,
        total
    })
    var xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)

    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf)
    xhr.onload = function(){
        if(this.status == 200){
            console.log("order placed")
            window.location = `/foodvilla/pay`
        }
        else{
         console.log("something went wrong")
        }

    }

    xhr.send(data)


}