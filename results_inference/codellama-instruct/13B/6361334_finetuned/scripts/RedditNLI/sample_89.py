sensex_premise = 103
sensex_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the same values for the Sensex and Nifty indices
if sensex_hypothesis!= sensex_premise or nifty_hypothesis!= nifty_premise:
    # check if the values in the hypothesis contradict the values in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the values in the premise, we can infer entailment
    label = "entailment"

print(label)
