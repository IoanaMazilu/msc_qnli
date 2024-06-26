distance_premise = 81
distance_hypothesis = 31

# the hypothesis refers to the distance Yolanda and Bob walked, mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise statement of less than 'distance_premise' miles
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
