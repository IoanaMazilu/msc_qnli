distance_premise = 800
distance_hypothesis = 500
speed_premise = 15
speed_hypothesis = 15

# the hypothesis talks about the same scenario as the premise, but with a different distance
if distance_hypothesis >= distance_premise:
    # check if the hypothesis distance contradicts the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
