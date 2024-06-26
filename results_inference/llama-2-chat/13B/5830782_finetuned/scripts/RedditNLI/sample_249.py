nifty_premise = 7500
nifty_hypothesis = 7400

# the hypothesis and premise mention the value of nifty
if nifty_premise < nifty_hypothesis:
    # check if the value of nifty in the hypothesis contradicts the value of nifty in the premise
    label = "contradiction"
elif nifty_premise > nifty_hypothesis:
    # check if the value of nifty in the premise contradicts the value of nifty in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
