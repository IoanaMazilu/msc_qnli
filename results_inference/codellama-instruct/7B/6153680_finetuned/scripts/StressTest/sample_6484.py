distance_premise = 80
distance_hypothesis = 20

# the hypothesis talks about the same distance between homes as the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives a maximum distance of 80 km
    # any distance less than 80 km is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
