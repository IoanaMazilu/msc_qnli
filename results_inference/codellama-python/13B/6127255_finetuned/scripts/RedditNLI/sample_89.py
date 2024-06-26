points_premise = 103
points_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the points and nifty value of the Sensex rise
if points_premise!= points_hypothesis:
    # check if the points in the hypothesis contradicts the points in the premise
    label = "contradiction"
elif nifty_premise!= nifty_hypothesis:
    # check if the nifty value in the hypothesis contradicts the nifty value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
