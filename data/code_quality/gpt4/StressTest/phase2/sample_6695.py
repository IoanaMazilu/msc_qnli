withdrawn_amount_premise = 14000
withdrawn_amount_hypothesis = 14000

# the hypothesis refers to the amount withdrawn by John after 8 months, mentioned in the premise
if withdrawn_amount_hypothesis >= withdrawn_amount_premise:
    # check if the hypothesis value contradicts the premise's claim of withdrawing less than 'withdrawn_amount_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise's claim, we can infer entailment
    label = "entailment"

print(label)
