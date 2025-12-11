from flask import Flask, render_template, request, redirect

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

@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    tarefas.pop(id)
    return redirect('/')

@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar_tarefa(id):
    tarefa = tarefas[id]

    if request.method == "POST":
        name = request.form["name"]

        tarefas[id] = {
            "id": tarefa["id"],
            "label": name,
            "finished": tarefa["finished"]
        }

        return redirect('/')

    return render_template('editar.html', tarefa=tarefa)

@app.route('/testes')
def render_testes():
    return render_template('teste.html')

champions = [
    {
      "version": "15.24.1",
      "id": "Aatrox",
      "key": "266",
      "name": "Aatrox",
      "title": "the Darkin Blade",
      "blurb": "Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...",
      "info": {
        "attack": 8,
        "defense": 4,
        "magic": 3,
        "difficulty": 4
      },
      "image": {
        "full": "Aatrox.png",
        "sprite": "champion0.png",
        "group": "champion",
        "x": 0,
        "y": 0,
        "w": 48,
        "h": 48
      },
      "tags": [
        "Fighter"
      ],
      "partype": "Blood Well",
      "stats": {
        "hp": 650,
        "hpperlevel": 114,
        "mp": 0,
        "mpperlevel": 0,
        "movespeed": 345,
        "armor": 38,
        "armorperlevel": 4.8,
        "spellblock": 32,
        "spellblockperlevel": 2.05,
        "attackrange": 175,
        "hpregen": 3,
        "hpregenperlevel": 0.5,
        "mpregen": 0,
        "mpregenperlevel": 0,
        "crit": 0,
        "critperlevel": 0,
        "attackdamage": 60,
        "attackdamageperlevel": 5,
        "attackspeedperlevel": 2.5,
        "attackspeed": 0.651
      }
    },
    {
      "version": "15.24.1",
      "id": "Ahri",
      "key": "103",
      "name": "Ahri",
      "title": "the Nine-Tailed Fox",
      "blurb": "Innately connected to the magic of the spirit realm, Ahri is a fox-like vastaya who can manipulate her prey's emotions and consume their essence—receiving flashes of their memory and insight from each soul she consumes. Once a powerful yet wayward...",
      "info": {
        "attack": 3,
        "defense": 4,
        "magic": 8,
        "difficulty": 5
      },
      "image": {
        "full": "Ahri.png",
        "sprite": "champion0.png",
        "group": "champion",
        "x": 48,
        "y": 0,
        "w": 48,
        "h": 48
      },
      "tags": [
        "Mage",
        "Assassin"
      ],
      "partype": "Mana",
      "stats": {
        "hp": 590,
        "hpperlevel": 104,
        "mp": 418,
        "mpperlevel": 25,
        "movespeed": 330,
        "armor": 21,
        "armorperlevel": 4.2,
        "spellblock": 30,
        "spellblockperlevel": 1.3,
        "attackrange": 550,
        "hpregen": 2.5,
        "hpregenperlevel": 0.6,
        "mpregen": 8,
        "mpregenperlevel": 0.8,
        "crit": 0,
        "critperlevel": 0,
        "attackdamage": 53,
        "attackdamageperlevel": 3,
        "attackspeedperlevel": 2.2,
        "attackspeed": 0.668
      }
    },
]

@app.route('/champions/<id>')
def render_champion(id):
    found_champion = None

    for champion in champions:
        if champion["id"] == id:
            found_champion = champion

    if found_champion is None:
        return redirect('/not-found')
    
    return render_template('champion.html', champion=champion)

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