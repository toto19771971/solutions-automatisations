from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "merguim"

EMAIL = "solutions.automatisations@gmail.com"
PASSWORD = "MOT_DE_PASSE_APPLICATION"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/realisations")
def realisations():
    return render_template("realisations.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/envoyer", methods=["POST"])
def envoyer():

    nom = request.form["nom"]
    entreprise = request.form["entreprise"]
    email = request.form["email"]
    telephone = request.form["telephone"]
    message = request.form["message"]

    corps = f"""
Nom : {nom}

Entreprise : {entreprise}

Email : {email}

Téléphone : {telephone}

Message :

{message}
"""

    msg = MIMEText(corps)

    msg["Subject"] = "Nouveau message depuis le site"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    serveur = smtplib.SMTP_SSL("smtp.gmail.com",465)

    serveur.login(EMAIL,PASSWORD)

    serveur.send_message(msg)

    serveur.quit()

    flash("Votre message a été envoyé.")

    return redirect("/contact")


if __name__ == "__main__":
    app.run(debug=True)