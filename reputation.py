reputation = {
    "Auditor1": 10,
    "Auditor2": 10,
    "Auditor3": 10,
    "Auditor4": 10,
    "Auditor5": 10
}

def update_reputation(votes, final_decision):

    for auditor,vote in votes.items():

        if vote == final_decision:
            reputation[auditor] += 1
        else:
            reputation[auditor] -= 1