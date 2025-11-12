from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Mi App Flask Bonita</title>
  <style>
    :root {
      --accent: #6C5CE7;
      --bg: #0f1724;
      --card: #0b1220;
      --muted: #98A8C7;
    }
    html,body {
      height: 100%;
      margin: 0;
      font-family: 'Inter', system-ui, sans-serif;
      background: linear-gradient(180deg, #071129 0%, #0A1829 100%);
      color: #E6EEF8;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .container {
      max-width: 900px;
      width: 90%;
      background: rgba(255, 255, 255, 0.05);
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
      text-align: center;
    }
    h1 {
      font-size: 2em;
      margin-bottom: 10px;
    }
    p {
      color: var(--muted);
    }
    button {
      margin-top: 20px;
      padding: 12px 20px;
      border: none;
      border-radius: 10px;
      background: var(--accent);
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: 0.2s;
    }
    button:hover {
      transform: scale(1.05);
      background: #7d68ff;
    }
    #mensaje {
      margin-top: 20px;
      color: #C7D7FF;
      font-weight: bold;
    }
    footer {
      margin-top: 30px;
      color: var(--muted);
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🚀 Bienvenido a mi App Flask</h1>
    <p>Esta app corre en Docker usando el puerto <strong>80</strong>.</p>
    <button id="boton">Saludar</button>
    <div id="mensaje">Haz clic en el botón 👆</div>
    <footer>© 2025 Flask Docker Demo</footer>
  </div>

  <script>
    document.getElementById('boton').addEventListener('click', async () => {
      const res = await fetch('/api/saludo');
      const data = await res.json();
      document.getElementById('mensaje').textContent = data.message;
    });
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/api/saludo')
def saludo():
    return jsonify({"message": "👋 Hola desde Flask en Docker!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
