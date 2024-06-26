pills_premise = 70e6
pills_hypothesis = 70e6
metal_premise = 200
metal_hypothesis = 200

# the hypothesis talks about the number of pills that contain metal, which is also mentioned in the premise
if metal_hypothesis!= metal_premise:
    # check if the number of pills with metal in the hypothesis contradicts the number of pills from the premise
    label = "contradiction"
elif pills_hypothesis!= pills_premise:
    # check if the number of pills in the hypothesis contradicts the number of pills in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
