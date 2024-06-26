nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the Nifty index traded above a certain level
if nifty_hypothesis < nifty_premise:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
else:
    # if the level in the hypothesis is greater or equal to the level in the premise, we can infer entailment
    label = "entailment"

print(label)
