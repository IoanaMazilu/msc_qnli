nifty_premise = 7500
nifty_hypothesis = 7400

# check if the hypothesis contradicts the premise
if nifty_hypothesis < nifty_premise:
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, so we can infer entailment
    label = "entailment"

print(label)
