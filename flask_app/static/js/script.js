



function hoverText(element) {
    if (element.style.boxShadow === "") {
        element.style.boxShadow = "10px 10px 10px #05386B"
        element.style.marginBottom = "10px"
    }
    else {
        element.style.boxShadow = ""
        element.style.marginBottom = ""
    }
}

function hoverLinks(element) {
    if (element.style.boxShadow === "") {
        element.style.boxShadow = "5px 5px 5px black"
        element.style.marginBottom = "5px"
    }
    else {
        element.style.boxShadow = ""
        element.style.marginBottom = ""
    }
}