from reputation import reputation

auditors = list(reputation.keys())

def vote(news_score):

    votes = {}

    for auditor in auditors:

        if news_score > 0.7:
            votes[auditor] = "Fake"
        elif news_score < 0.3:
            votes[auditor] = "Real"
        else:
            votes[auditor] = "Uncertain"

    return votes