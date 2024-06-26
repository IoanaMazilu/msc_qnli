nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the value of the Nifty
if nifty_hypothesis >= nifty_premise:
    # check if the value of the Nifty in the hypothesis contradicts the value of the Nifty in the premise
    label = "contradiction"
else:
    # if the value of the Nifty in the hypothesis is less than the value of the Nifty in the premise, we can infer entailment
    label = "entailment"

print(label)
