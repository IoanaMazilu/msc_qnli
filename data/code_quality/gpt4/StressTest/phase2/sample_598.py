distance_premise = 77
distance_hypothesis = 17

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise' miles
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
