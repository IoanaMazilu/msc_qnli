distance_covered_premise = 800
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis talks about the time Sandy takes to cover a certain distance, referenced also in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_covered_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
