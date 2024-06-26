distance_premise = 800
distance_hypothesis = 100

# the hypothesis refers to the distance between Fred and Sam mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis is less than the distance reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)