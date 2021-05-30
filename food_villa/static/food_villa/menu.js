document.querySelectorAll('.addCart').forEach(item =>{
    item.addEventListener('click', updateCart)
})

function updateCart(e){
    e.preventDefault()
    var id = e.target.parentElement.parentElement.id
    var url = document.querySelector('#cartIcon').dataset.url
    var csrf = document.querySelector('#cartIcon').dataset.csrf

    var xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)

    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf)

    data = JSON.stringify({
        id: id
    })

    xhr.onload = function(){
        if(this.status == 200){
            cartCount = parseInt(document.querySelector('#cartInfo').innerHTML )
            document.querySelector('#cartInfo').innerHTML = cartCount + 1
        }
        else{
            console.log('Some error occurred..Try again.')
        }
    }

    xhr.send(data)
   
}