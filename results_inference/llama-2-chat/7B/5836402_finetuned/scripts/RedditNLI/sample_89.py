points_premise = 103
points_hypothesis = 100

# the hypothesis and premise mention the rise in Sensex points and the ending point of Nifty
if points_hypothesis!= points_premise:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
