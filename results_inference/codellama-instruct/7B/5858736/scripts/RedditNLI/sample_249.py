nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the Nifty index trading above a certain level
if nifty_hypothesis < nifty_premise:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
