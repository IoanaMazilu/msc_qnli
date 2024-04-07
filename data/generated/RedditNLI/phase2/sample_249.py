# Premise: Nifty traded above 7500, Trading Calls Today.
# Hypothesis: Nifty above 7400,
# Golden Label: entailment

nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the value at which Nifty is trading
if nifty_hypothesis > nifty_premise:
    # check if the Nifty value in the hypothesis contradicts the Nifty value in the premise
    label = "contradiction"
elif nifty_hypothesis < nifty_premise:
    # the hypothesis value of Nifty is less than the premise value, which is consistent but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the Nifty value in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

