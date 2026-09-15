async function carregarDashboard() {
    const response = await fetch("/api/dashboard");
    const data = await response.json();

    document.getElementById("clientes").textContent = data.clientes;
    document.getElementById("pedidos").textContent = data.pedidos;
    document.getElementById("concluidos").textContent = data.pedidos_concluidos;

    document.getElementById("faturamento").textContent =
        data.faturamento.toLocaleString("pt-BR", {
            style: "currency",
            currency: "BRL"
        });
}


async function carregarClientes(busca = "") {
    const response = await fetch(
        `/api/clientes?busca=${encodeURIComponent(busca)}`
    );

    const clientes = await response.json();

    const tabela = document.getElementById("clientes-table");

    tabela.innerHTML = "";

    clientes.forEach(cliente => {

        tabela.innerHTML += `
            <tr>
                <td>${cliente.nome}</td>
                <td>${cliente.email}</td>
                <td>${cliente.empresa}</td>
            </tr>
        `;
    });
}


async function carregarPedidos() {
    const response = await fetch("/api/pedidos");
    const pedidos = await response.json();

    const tabela = document.getElementById("pedidos-table");

    tabela.innerHTML = "";

    pedidos.forEach(pedido => {

        tabela.innerHTML += `
            <tr>
                <td>#${pedido.id}</td>
                <td>${pedido.cliente}</td>
                <td>${pedido.produto}</td>
                <td>${pedido.valor.toLocaleString("pt-BR", {
                    style: "currency",
                    currency: "BRL"
                })}</td>
                <td>
                    <span class="status">
                        ${pedido.status}
                    </span>
                </td>
            </tr>
        `;
    });
}


function buscarClientes() {
    const busca = document.getElementById("search").value;
    carregarClientes(busca);
}


function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });
}


carregarDashboard();
carregarClientes();
carregarPedidos();
