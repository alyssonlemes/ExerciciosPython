principal()

//escrita de função na versão nova do javascript, torna as funções = variáveis
let principal = () => {
    let vetFarmacias = []
    let vetRemedios = []
    let opcao
    do {
        opcao = Number(prompt("Escolha uma opção:\n1 - Cadastrar Farmácias\n2 - Cadastrar Remédios\n3 - Realizar Venda de Remédios\n4 - Sair"))
        switch (opcao) {
            case 1:
                cadastraFarmacias(vetFarmacias)
                break
            case 2:
                cadastraRemedios(vetRemedios, vetFarmacias)
                break
            case 3:
                vendaRemedios(vetRemedios)
                break
            case 4:
                alert("Encerrando o programa.")
                break
            default:
                alert("Opção inválida. Tente novamente.")
        }
    } while (opcao !== 4)
}


let cadastraFarmacias = (vetFarmacias) => {
    for(let i=0;i<5;i++){
        let novaFarmacia = {
            codigo: Number(prompt('Código da farmacia')),
            nome: prompt('Nome da farmácia'),
            endereco: prompt('Endereço da farmácia')
        }
        // verificar se o código da novaFarmácia está no vetor
        // percorre o vetor vetFarmacias procurando por código já existente
        while (vetFarmacias.some((farm) => farm.codigo == novaFarmacia.codigo)){
            novaFarmacia.codigo = Number(prompt('Código já existe, informe um novo'))
        }
        vetFarmacias.push(novaFarmacia)
    }
}

let cadastraRemedios = (vetRemedios, vetFarmacias) => {
    for(let i=0;i<5;i++){
        let novoRemedio = {
            codigoFarmacia: Number(prompt('Código da farmácia')),
            nome: prompt('Nome do remédio'),
            qtde: Number('Qtde do remédio'),
            preco: Number('Preço do remédio')
        }
        // ! é negação
        while(!vetFarmacias.some((farm) => farm.codigo == novoRemedio.codigoFarmacia)){
            novoRemedio.codigoFarmacia = Number(prompt('Farmácia não existe. Digite novamente'))
        }
        vetRemedios.push(novoRemedio)
    }
}

let vendaRemedios = (vetRemedios) => {
    for(let cont = 0; cont < 5; i++){
    let objVenda = {
        codigoFarmacia: Number(prompt('Código do remédio')),
            nome: prompt('Nome do remédio'),
            qtde: Number('Qtde do remédio')
    }
    //percorre o vetor vetRemedios procurando pelo código
    // do remedio e o nome do remedio
    let achou = false //nao encontrei o remedio
    for(let i = 0; i < vetRemedios.lenght; i++){
        if(vetRemedios[i].codigoFarmacia == objVenda.codigo && vetRemedios[i].nome == objVenda.nome){
           achou = true//achei o remedio 
           //vamos realizar a venda
           if(vetRemedios[i].qtde >= objVenda.qtde){
                vetRemedios[i].qtde = vetRemedios[i].qtde - objVenda.qtde
           }
        }
        else{
            alert("Estoque insuficiente para essa venda")
        }

    }
    if(!achou){
        alert("Produto não encontrado!")
    }
}}