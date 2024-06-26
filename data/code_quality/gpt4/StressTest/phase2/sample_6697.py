withdraw_premise = 5000
withdraw_hypothesis = 2000

# the hypothesis refers to the amount Tony withdraws, also mentioned in the premise
if withdraw_hypothesis >= withdraw_premise:
    # check if the hypothesis value contradicts the estimate of less than 'withdraw_premise'
    label = "contradiction"
elif withdraw_hypothesis < withdraw_premise:
    # if the hypothesis value is less than 'withdraw_premise', we can infer entailment
    label = "entailment"

print(label)
