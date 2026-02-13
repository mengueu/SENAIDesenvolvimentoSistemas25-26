var contadorAluno = 0;
function cadastrarAluno() {
    contadorAluno++;

    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let ra = document.getElementById("ra").value;
    let telefone = document.getElementById("telefone").value;
    let turma = document.getElementById("turma").value;

    let lista = document.createElement("li");
    lista.setAttribute("id", "aluno" + contadorAluno);

    lista.innerHTML =
    "<strong>Aluno " + contadorAluno + "</strong>" +
    "<ul class='dados-aluno'>" +
    "<li>Nome: " + nome + "</li>" +
    "<li>Email: " + email + "</li>" +
    "<li>RA: " + ra + "</li>" +
    "<li>Telefone: " + telefone + "</li>" +
    "<li>Turma: " + turma + "</li>" +
    "</ul>";

    let botaoExcluir = document.createElement("button");
    botaoExcluir.textContent = "Excluir";
    botaoExcluir.setAttribute("onclick", "removerAluno(" + contadorAluno + ")");

    lista.appendChild(document.createTextNode(" "));
    lista.appendChild(botaoExcluir);

    document.getElementById("listaAlunos").appendChild(lista);

    document.getElementById("formCadastro").reset();
}
function removerAluno(idAluno) {
    var aluno = document.getElementById("aluno" + idAluno);
    document.getElementById("listaAlunos").removeChild(aluno);
}
