distance_walked_premise = 30
distance_walked_hypothesis = 10

# the hypothesis refers to the distance walked from X to Y, also mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_walked_premise'
    label = "contradiction"
elif distance_walked_hypothesis < distance_walked_premise:
    # the premise gives only an estimate for the distance of less than 'distance_walked_premise'
    # any distance less than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
