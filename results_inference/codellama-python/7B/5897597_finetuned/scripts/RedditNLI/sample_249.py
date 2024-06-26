nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the level of Nifty
if nifty_hypothesis > nifty_premise:
    # check if the level of Nifty in the hypothesis contradicts the level of Nifty in the premise
    label = "contradiction"
elif nifty_hypothesis < nifty_premise:
    # check if the level of Nifty in the hypothesis is less than the level of Nifty in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
