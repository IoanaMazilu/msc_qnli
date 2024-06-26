premise_shorts = 13.99
premise_shirt = 12.14
premise_jacket = 7.43
hypothesis_net_amount = 17.5

# the hypothesis refers to the net amount of money spent on clothes, which is a sum of the premise values
# compute the total amount of money spent on clothes
total_amount_spent = premise_shorts + premise_shirt + premise_jacket
if total_amount_spent!= hypothesis_net_amount:
    # check if the total amount of money spent on clothes contradicts the net amount of money from the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
