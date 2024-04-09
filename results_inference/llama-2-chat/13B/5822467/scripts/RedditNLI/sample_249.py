nifty_premise = 7500
nifty_hypothesis = 7400

# the premise and hypothesis mention a specific value of Nifty
if nifty_premise!= nifty_hypothesis:
    # check if the value in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the values are the same, we can infer entailment
    label = "entailment"

print(label)
