distance_traveled_premise = 1/2
distance_traveled_hypothesis = 8/2

# the hypothesis talks about the distance traveled by Maria during a car trip, which is also mentioned in the premise
if distance_traveled_premise >= distance_traveled_hypothesis:
    # check if the hypothesis value contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the distance traveled in the hypothesis is less than the distance traveled in the premise, we can infer entailment
    label = "entailment"

print(label)
