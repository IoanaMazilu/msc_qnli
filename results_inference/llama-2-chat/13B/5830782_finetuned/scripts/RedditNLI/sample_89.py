sensex_rise_premise = 103
sensex_rise_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the Sensex rise, Nifty value and a tip related to stocks
if sensex_rise_premise!= sensex_rise_hypothesis:
    # check if the Sensex rise in the hypothesis contradicts the Sensex rise in the premise
    label = "contradiction"
elif nifty_premise!= nifty_hypothesis:
    # check if the Nifty value in the hypothesis contradicts the Nifty value in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
