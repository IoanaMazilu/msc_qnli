premise_amount = 2000
hypothesis_amount = 7000

# the hypothesis refers to the amount of money withdrawn by Tony
if premise_amount <= hypothesis_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount of money withdrawn in the premise
    label = "contradiction"
elif hypothesis_amount - premise_amount > 5000:
    # check if the difference between the hypothesis and premise amounts contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
