distance_premise = 120
distance_hypothesis = 620
rate_premise = 30
rate_hypothesis = 30

# the hypothesis refers to the distance and average rate of the train travel mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # check if the distance in the hypothesis exactly equals the distance in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
