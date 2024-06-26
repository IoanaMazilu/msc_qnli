sensex_premise = 103
sensex_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the rise of Sensex and Nifty
if sensex_hypothesis!= sensex_premise:
    # check if the rise of Sensex in the hypothesis contradicts the rise of Sensex in the premise
    label = "contradiction"
elif nifty_hypothesis!= nifty_premise:
    # check if the rise of Nifty in the hypothesis contradicts the rise of Nifty in the premise
    label = "contradiction"
else:
    # if the rise of Sensex and Nifty in the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
