diameter_premise = 100
diameter_hypothesis = 100
distance_premise = 26500
distance_hypothesis = 26500

# the hypothesis talks about the diameter and distance of the asteroid, which are also mentioned in the premise
if diameter_hypothesis!= diameter_premise:
    # check if the diameter in the hypothesis contradicts the diameter in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
