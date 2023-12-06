var database = require("../database/config");

function buscarPalavrasWordCloud() {
  
    var instrucao = `SELECT palavraGrossa AS palavra, quantidadeTotalAtual AS total FROM grosseria`;

    // console.log("Executando a instrução SQL: \n" + instrucao);
    return database.executar(instrucao);
}

function kpiMesAtual(){
    instrucao = `SELECT SUM(quantidadeTotalAtual) AS mesAtual FROM grosseria`;
    return database.executar(instrucao);
}

function kpiMesPassado(){
    instrucao = `SELECT SUM(quantidadeTotalPassado)AS mesPassado FROM grosseria`;
    return database.executar(instrucao);
}

module.exports = {
    buscarPalavrasWordCloud,
    kpiMesAtual,
    kpiMesPassado,
}