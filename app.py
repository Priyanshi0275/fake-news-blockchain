from flask import Flask,render_template,request
from blockchain import Blockchain,Block
from mlmodel import predict_news
from auditor import vote
from consensus import select_validator
from reputation import update_reputation,reputation

app = Flask(__name__)

blockchain = Blockchain()


@app.route("/")
def home():

    return render_template("index.html",chain=blockchain.chain,reputation=reputation)


@app.route("/submit",methods=["POST"])
def submit():

    news = request.form["news"]

    score = predict_news(news)

    votes = vote(score)

    fake_votes = list(votes.values()).count("Fake")
    real_votes = list(votes.values()).count("Real")

    final = "Fake" if fake_votes > real_votes else "Real"

    validator = select_validator()

    prev_block = blockchain.chain[-1]

    new_block = Block(
        len(blockchain.chain),
        news,
        score,
        validator,
        votes,
        prev_block.hash
    )

    blockchain.add_block(new_block)

    update_reputation(votes,final)

    return render_template(
        "index.html",
        chain=blockchain.chain,
        score=score,
        votes=votes,
        decision=final,
        validator=validator,
        reputation=reputation
    )


if __name__ == "__main__":
    app.run(debug=True)