total_spent_premise = 145.16 - 5.84
total_spent_hypothesis = 134.7

# the hypothesis refers to the total amount that Mike spent, which is also mentioned in the premise
# check if the total amount in the hypothesis contradicts the total amount from the premise
if total_spent_hypothesis!= total_spent_premise:
    # if the total amount in the hypothesis contradicts the total amount from the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the total amount in the hypothesis does not contradict the total amount from the premise, we can infer entailment
    label = "entailment"

print(label)