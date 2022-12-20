async function carregarAnimais(){

    // Requisitando endpoint API
    const response = await axios.get('http://127.0.0.1:8000/animais')
    
    // Passando parametros da requisicão
    const animais = response.data
    
    // Buscando ID nas tag HTML
    const lista = document.getElementById('lista-animais')
    
    // Especificando qual extensão do arquivo
    lista.innerHTML('')

    // Iterando 'stdout' para o frontend
    animais.array.forEach(animal => {
        
        // A tag que o id 'lista-animais' se encontra é <ul> portando criamos o elemento do tipo 'li' 
        const item = document.createElement('li')

        // Gerando 'stdout' no frontend
        const line = `${animal.nome}- Nome ${animal.idade} - Idade ${animal.sexo} - Sexo ${animal.peso} - Peso`

        // Instânciando como texto
        item.innerText = line

        // Instânciando para elemento criado gerando saída
        lista.appendChild(item)

    });
}

function manipularFormulario(){
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')

    // Instânciando API a partir frontend
    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value

        await axios.post('http://127.0.0.1:8000/animais', {
            nome: nome_animal,
            idade: 4,
            sexo: 'femea',
            cor: 'branco',
            peso: 8
        })
        carregarAnimais()
        alert('Animal Cadastrado')

    }
}

// Principal chamada das funcões do arquivo
function main(){
    console.log('App Iniciada')
    carregarAnimais()
    manipularFormulario()
}

main()
