let principal = () => {
    // votação
    for(let i=0;i<10;i++){
        let codigoPartidoVotado = Number(prompt(`Código do partido`))
        let nomePolíticoVotado = prompt(`Nome do político`).toUpperCase()
        let achou = false
        for(let j=0;j<politicos.length;j++){
            if ((politicos[j].codigoPartido == codigoPartidoVotado) &&
               (politicos[j].nome == nomePolíticoVotado)){
                politicos[j].qtde++
                alert(`Voto computador, acredite em mim`)
                achou = true
                break
            } 
        }
        if (!achou){
            alert(`Voto inválido`)
            i--
        }
    }
    
}

let cadastro = () => {
    // cadastra partidos
    let partidos = []
    for(let i=0;i<5;i++){
        let objPartido = {
            codigo: Number(prompt(`Informe código do partido`)),
            nome: prompt(`Informe nome do partido`),
            sigla: prompt(`Informe sigla do partido`),
            presidente: prompt(`Informe presidente do partido`),
            qtdePoliticos: Number(prompt(`Informe qtde de políticos `))
        }
        let achou = false
        for(let j=0;j<partidos.length;j++){
            if (partidos[j].codigo == objPartido.codigo){
                achou = true // não pode inserir
                break// não continua procurando
            }
        }
        if (!achou){
            partidos.push(objPartido)
            alert(`Partido inserido com sucesso`)
        }
        else {
            alert(`Código do partido já existe`)
            i--
        }
    }
}