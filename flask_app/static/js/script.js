



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