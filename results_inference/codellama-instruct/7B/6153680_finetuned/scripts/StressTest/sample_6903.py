total_payment_premise = 160
total_payment_hypothesis = 360

# the hypothesis refers to the total payment Rahul made for renting the tool, which is also mentioned in the premise
if total_payment_hypothesis <= total_payment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
