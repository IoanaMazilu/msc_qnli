total_amount_premise = 6600
total_amount_hypothesis = 6600

# the hypothesis refers to the total amount among John, Jose and Binoy, which is also mentioned in the premise
if total_amount_hypothesis!= total_amount_premise:
    # check if the total amount in the hypothesis contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the total amount in the hypothesis does not contradict the total amount in the premise, we can infer entailment
    label = "entailment"

print(label)
