# ====== DADOS DA PÁGINA ======
titulo = "Aprenda a se tornar um Fotógrafo Profissional"
descricao = "Descubra como transformar sua paixão por fotografia em uma carreira de sucesso."
botao = "Quero Começar Agora"

html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Curso de Fotografia</title>

    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #1e1e1e;
            color: white;
            text-align: center;
        }}

        .container {{
            padding: 60px 20px;
        }}

        h1 {{
            font-size: 40px;
        }}

        p {{
            font-size: 18px;
            max-width: 600px;
            margin: 20px auto;
        }}

        .lista {{
            margin-top: 30px;
        }}

        .lista li {{
            margin: 10px 0;
        }}

        .botao {{
            display: inline-block;
            margin-top: 30px;
            padding: 12px 30px;
            font-size: 18px;
            background-color: #ff9800;
            color: black;
            text-decoration: none;
            border-radius: 5px;
        }}

        footer {{
            margin-top: 50px;
            padding: 20px;
            background-color: #111;
        }}
    </style>
</head>

<body>

    <div class="container">
        <h1>{titulo}</h1>

        <p>{descricao}</p>

        <h2>O que você vai aprender:</h2>

        <ul class="lista" style="list-style: none;">
            <li>✔ Como usar o modo manual da câmera</li>
            <li>✔ Técnicas de iluminação profissional</li>
            <li>✔ Edição básica e avançada</li>
            <li>✔ Como conseguir seus primeiros clientes</li>
        </ul>

        <a href="#" class="botao">{botao}</a>
    </div>

    <footer>
        <p>© 2026 Curso de Fotografia Profissional</p>
    </footer>

</body>
</html>
"""