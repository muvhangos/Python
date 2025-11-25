from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/create", methods=["POST"])
def create():
    item = request.form.get("item")
    if item:
        items.append(item)
    return redirect(url_for("index"))

@app.route("/update/<int:index>", methods=["GET", "POST"])
def update(index):
    if request.method == "POST":
        items[index] = request.form.get("item")
        return redirect(url_for("index"))
    return render_template("update.html", item=items[index], index=index)

@app.route("/delete/<int:index>")
def delete(index):
    items.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
