distance_premise = 500
distance_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance covered by Sandy, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the distance covered in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance covered by Sandy
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
