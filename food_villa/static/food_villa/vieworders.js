

const feedForm = document.querySelector('#feedbackform')
const feedsubmit = document.querySelector('.submitfeed')
const feedtext = document.querySelector('#feedbacktext')
const validator = document.querySelector('#validator')
var feed_id = -1

document.querySelectorAll(".feed").forEach(i =>{
    i.addEventListener('click', (e)=>{
        document.querySelector('.header').style.filter = "blur(2px)"
        document.querySelector('.orderTable').style.filter = "blur(2px)"
        feedForm.style.display = "block"
        feed_id = e.target.id
    })
})

document.querySelector('.cross').addEventListener('click', ()=>{
    document.querySelector('.header').style.filter = "blur(0px)"
    document.querySelector('.orderTable').style.filter = "blur(0px)"
    feedForm.style.display = "none"
})


feedForm.addEventListener('mouseover', ()=>{
    document.querySelector('.cross').style.display = "block"
})
feedForm.addEventListener('mouseout', ()=>{
    document.querySelector('.cross').style.display = "none"
})

feedsubmit.onclick = (e)=>{
    e.preventDefault()
    if(feedtext.value == ""){
        validator.innerHTML = "No value entered"
        validator.style.display = "block"
        setTimeout(()=>{
            validator.style.display = "none"
        },3000)
        return
    }

    data = JSON.stringify({
        feedback: feedtext.value,
        id: feed_id
    })

    url = e.target.dataset.url
    csrf = e.target.dataset.csrf

    var xhr = new XMLHttpRequest()

    xhr.open('POST', url , true)
    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf)

    xhr.onload = function(){
        if(this.status == 200){
            validator.innerHTML = "Feedback Submitted"
            validator.style.display = "block"
            setTimeout(()=>{
                validator.style.display = "none"
            },5000)
        }
        else{
            validator.innerHTML = "Some error occured"
            validator.style.display = "block"
            setTimeout(()=>{
                validator.style.display = "none"
            },5000)
        }
        document.querySelector('.header').style.filter = "blur(0px)"
        document.querySelector('.orderTable').style.filter = "blur(0px)"
        feedtext.value = ""
        feedForm.style.display = "none"
    }

    xhr.send(data)



}
