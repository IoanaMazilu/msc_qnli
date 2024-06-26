distance_traveled_premise = 1/2
distance_traveled_hypothesis = 8/2

# the hypothesis refers to the distance traveled by Maria during a car trip, which is also mentioned in the premise
if distance_traveled_premise >= distance_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the estimate of less than 'distance_traveled_hypothesis'
    label = "contradiction"
else:
    # if the distance traveled in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
