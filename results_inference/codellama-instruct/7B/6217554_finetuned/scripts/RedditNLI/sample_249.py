nifty_premise = 7500
nifty_hypothesis = 7400

if nifty_hypothesis >= nifty_premise:
    # check if the Nifty value in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the Nifty value in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
