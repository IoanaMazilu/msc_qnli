asteroid_diameter_premise = 100
asteroid_diameter_hypothesis = 100

# the hypothesis talks about the diameter of the asteroid which is also mentioned in the premise
if asteroid_diameter_hypothesis!= asteroid_diameter_premise:
    # check if the diameter of the asteroid in the hypothesis contradicts the diameter of the asteroid from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
