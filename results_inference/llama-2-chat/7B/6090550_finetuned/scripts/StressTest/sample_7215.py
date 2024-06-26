y = 60
x = 20

distance_premise = 480
distance_hypothesis = 480

# the hypothesis talks about the fuel tank size and the distance to Cleveland, both mentioned in the premise
if x!= 20:
    # check if the fuel tank size in the hypothesis contradicts the fuel tank size in the premise
    label = "contradiction"
elif y!= 60:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
