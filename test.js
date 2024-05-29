const btn = document.querySelector('#button')

btn.addEventListener('click', () => {
    replaced_code = document.querySelector('.code').value.replaceAll(" ", "_").replaceAll('"', "'").replaceAll("\n", "\\n").replaceAll("\t", "\\t")
    console.log(document.querySelector('.code').value)
    console.log(`replaced: ${replaced_code}`)
    SendData(replaced_code)
})

function editDiv(result) {
    const element = document.querySelector('.response')
    element.innerText = result
}


function SendData(code) {
    ob = {
        command: code,
        target: 'py'
    }
    console.log(JSON.stringify(ob))
    console.log(`입력된 code: ${code}`)
    fetch('http://localhost:8888', {
        method: 'POST',
        body: JSON.stringify(ob),
        headers: {'Content-Type': 'application/json'}
    })
        .then((response) => response.text())
        .then((result) => {editDiv(JSON.parse(result).response);})
}