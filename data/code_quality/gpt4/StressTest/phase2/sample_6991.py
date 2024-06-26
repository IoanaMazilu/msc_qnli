distance_premise = 52
distance_hypothesis = 12

# the hypothesis refers to the distance run by the sisters, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance run by the sisters
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
