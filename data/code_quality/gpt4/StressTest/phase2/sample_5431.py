charges_per_transaction_premise = 0.75
transactions_premise = 7
charges_per_transaction_hypothesis = 0.75
transactions_hypothesis = 3

# the hypothesis refers to the bank charges for transactions mentioned in the premise
if charges_per_transaction_premise != charges_per_transaction_hypothesis:
    # check if the charges per transaction in the hypothesis contradicts the charges per transaction in the premise
    label = "contradiction"
elif transactions_hypothesis >= transactions_premise:
    # check if the number of transactions in the hypothesis contradicts the number of transactions in the premise
    label = "contradiction"
else:
    # the premise gives a threshold for the number of transactions
    # any number of transactions less than 'transactions_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
