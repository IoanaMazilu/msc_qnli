distance_premise = 800
distance_hypothesis = 500
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance covered by Sandy, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered by Sandy
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
