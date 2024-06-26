points_rise_premise = 103
points_rise_hypothesis = 100
nifty_end_premise = 8900
nifty_end_hypothesis = 8900

# the hypothesis and premise mention the points that Sensex rises, the Nifty ends and the stock tips tomorrow
if points_rise_premise!= points_rise_hypothesis:
    # check if the points that Sensex rises in the hypothesis contradicts the points that Sensex rises in the premise
    label = "contradiction"
elif nifty_end_premise!= nifty_end_hypothesis:
    # check if the Nifty end value in the hypothesis contradicts the Nifty end value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
