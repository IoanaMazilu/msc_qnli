total_paid_premise = 160
total_paid_hypothesis = 360

# the hypothesis refers to the total amount paid to rent the tool, which is also mentioned in the premise
if total_paid_hypothesis <= total_paid_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
