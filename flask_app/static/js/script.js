



function hoverText(element) {
    console.log(element.style)
    if (element.style.textShadow === "") {
        element.style.textShadow = "10px 10px 10px #05386B"
        element.style.position = "relative"
        element.style.bottom = "5px"
    }
    else {
        element.style.textShadow = ""
        element.style.position = ""
        element.style.bottom = ""
    }
}

function hoverLinks(element) {
    console.log(element.style.shadow)
    if (element.style.textShadow === "") {
        element.style.textShadow = "5px 5px 5px black"
        element.style.position = "relative"
        element.style.bottom = "2px"
    }
    else {
        element.style.textShadow = ""
        element.style.position = ""
        element.style.bottom = ""
    }
}

function navigateToRoute(id) {
    console.log(id)
    fetch(`/view/ltg/${id}`, {
        method: 'GET'
    })
    .then(response => {
        window.location.href = response.url
    })
    .catch(error => {
        console.error('Error: ', error)
    })
    
}