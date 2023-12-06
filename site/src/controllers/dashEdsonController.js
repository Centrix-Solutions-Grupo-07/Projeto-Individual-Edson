var edsonModel = require("../models/dashboardEdsonModel");

function buscarPalavrasWordCloud(res, res) {
    edsonModel.buscarPalavrasWordCloud().then(function (resultado) {
        if (resultado == undefined) {
            res.status(204).send("Nenhuma palavra encontrada!");
        }else{
            res.status(200).json(resultado);
        }
    }).catch(function(erro){
        console.log(erro);
        console.log("Houve um erro ao buscar pelas palavras ", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

function kpiMesAtual(res, res){
    edsonModel.kpiMesAtual().then(function (resultado){
        if (resultado == undefined) {
            res.status(204).send("Nenhuma palavra encontrada!")
        }else{
            res.status(200).json(resultado);
        }
    }).catch(function(erro){
        console.log(erro);
        console.log("Houve um erro ao buscar pelas palavras ", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

function kpiMesPassado(res, res){
    edsonModel.kpiMesPassado().then(function (resultado){
        if (resultado == undefined) {
            res.status(204).send("Nenhuma palavra encontrada!")
        }else{
            res.status(200).json(resultado);
        }
    }).catch(function(erro){
        console.log(erro);
        console.log("Houve um erro ao buscar pelas palavras ", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

module.exports = {
    buscarPalavrasWordCloud,
    kpiMesAtual,
    kpiMesPassado,
}