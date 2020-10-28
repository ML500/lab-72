const BASE_URL = 'http://localhost:8000/';
const BASE_API_URL = BASE_URL + 'api/';


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return response;
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}


    let main = document.getElementById('main');
    let cont = document.getElementById('container');



    const addAll = async () =>{
        let data = await makeRequest('http://localhost:8000/api/quote/')
        cont.innerText = ""
        data = await data.json();
        for(let i=0; i < data.length; i++) {

            let child = document.createElement('a')
            child.innerText = `Text: ${data[i].text}`
            child.style.display ='block'
            child.setAttribute("href", BASE_API_URL + 'quote/' + data[i].id)
            cont.append(child)
        }
    }

    main.addEventListener('click',async function (event) {
        event.preventDefault()
        await addAll()
    })


