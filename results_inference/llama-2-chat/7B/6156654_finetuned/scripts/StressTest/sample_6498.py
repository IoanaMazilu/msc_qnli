distance_matthew = 45
distance_hypothesis = 35

# the hypothesis talks about the distance Matthew walked, which is also mentioned in the premise
if distance_hypothesis <= distance_matthew:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is greater than the distance in the premise, it does not contradict the premise
    # but it also cannot be explicitly entailed from the premise, so we label it as neutral
    label = "neutral"

print(label)
