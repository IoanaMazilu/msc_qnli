distance_premise = 800
distance_hypothesis = 500
speed_premise = 15
speed_hypothesis = 15

# the hypothesis talks about the time Sandy takes to cover a certain distance, also referenced in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis distance contradicts the premise's estimate of less than 'distance_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
