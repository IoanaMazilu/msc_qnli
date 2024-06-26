sensex_rise_premise = 103
sensex_rise_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the rise of the Sensex and the Nifty
# however, the hypothesis mentions the rise of the Sensex as 100 pts, which is less than the premise of 103 pts
if sensex_rise_hypothesis!= sensex_rise_premise:
    # check if the rise of the Sensex in the hypothesis contradicts the rise of the Sensex in the premise
    label = "contradiction"
elif nifty_hypothesis!= nifty_premise:
    # check if the Nifty value in the hypothesis contradicts the Nifty value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
