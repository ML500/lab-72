
window.onload = async function() {
    let add = document.getElementById('add');
    let cont = document.getElementById('container');
    add.addEventListener('click',  function (event) {
        event.preventDefault()
        cont.innerText = ""
        let form = document.createElement("form");
            form.setAttribute("method", "post");
            form.addEventListener("submit", async function (event) {
                event.preventDefault()
                let data = {
                    text:document.getElementById("text").value,
                    author:document.getElementById("author").value,
                    email: document.getElementById("email").value,
                }
                let response = await makeRequest(BASE_API_URL + 'quote/', "POST", data )
                let quote = await response.json();
                await addAll()
                alert("создана новая цитата " + quote.text)
            })
        let text = document.createElement("input");
            text.setAttribute("name", "text");
            text.setAttribute("type", "text");
            text.setAttribute("placeholder", "text");
            text.id = "text"
            text.style.display ='block'

        let author = document.createElement("input");
            author.setAttribute("name", "text");
            author.setAttribute("type", "text");
            author.setAttribute("placeholder", "author");
            author.id="author"
            author.style.display ='block'
        let email = document.createElement("input");
            email.setAttribute("name", "email");
            email.setAttribute("type", "text");
            email.setAttribute("placeholder", "email");
            email.id = "email"
            email.style.display ='block'
        let submit = document.createElement("input");
                submit.setAttribute("type", "submit");
                submit.setAttribute("value", "Submit");
        form.appendChild(text);
        form.appendChild(author);
        form.appendChild(email);
        form.appendChild(submit);
        cont.appendChild(form)
    })
}