decrease_percentage_premise = 30
decrease_percentage_hypothesis = 80
current_balance = 100

# the hypothesis refers to the percentage decrease in saving amount due to loan payment, which is also mentioned in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif current_balance!= 100:
    # check if the current balance in the hypothesis contradicts the current balance in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
