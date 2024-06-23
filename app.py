from flask import Flask, render_template
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def prueba():
    html = render_template('plantilla.html')
    return render_pdf(HTML(string=html))

if __name__ == '__main__':
    app.run(debug=True)