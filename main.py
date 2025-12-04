from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "label": "Dar aula sobre métodos HTTP",
        "finished": False
    },
    {
        "id": 2,
        "label": "Dar aula sobre métodos HTTP",
        "finished": False
    }
]

@app.route('/', methods=['GET', 'POST'])
def render_tarefas():
    print(request.method)

    if request.method == "POST":
        name = request.form["name"]

        if len(name) == 0:
            return render_template(
                'tarefas.html', 
                tarefas=tarefas, 
                erro="Nome é obrigatório"
            )

        id = tarefas[-1]["id"] + 1
        tarefas.append({
            "id": id,
            "label": name,
            "finished": False
        })

    return render_template('tarefas.html', tarefas=tarefas)

produtos = [
    {
        "id": 1,
        "name": "Tenis da Nike",
        "price": 500,
        "reviews": 4.7,
        "warranty": 3
    },
    {
        "id": 2,
        "name": "Tenis da Adidas",
        "price": 300,
        "reviews": 4.9,
        "warranty": 6
    },
    {
        "id": 3,
        "name": "Tenis da Rebook",
        "price": 25,
        "reviews": 4.1,
        "warranty": 1
    }
]

@app.route('/produtos/<product_id>')
def render_product(product_id):
    produto_encontrado = None

    for produto in produtos:
        if produto["id"] == int(product_id):
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        return render_template('produto_nao_encontrado.html')

    return render_template('produto.html', produto=produto_encontrado)

app.run(debug=True)