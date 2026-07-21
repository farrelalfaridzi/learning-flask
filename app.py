from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def home():
    return render_template(
        "index.html",
        nama="Farrel",
        umur=18,
        jurusan="Teknik Informatika",
        saldo=0,
        hobi=[
            "Ngoding",
            "Main Game",
            "Belajar Linux"
        ]
    )

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        jumlah = request.form["jumlah"]
        kategori = request.form["kategori"]
        catatan = request.form["catatan"]
        if jumlah == "":
            return "jumlah tidak boleh kosong"
        print(jumlah)
        print(kategori)
        print(catatan)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)