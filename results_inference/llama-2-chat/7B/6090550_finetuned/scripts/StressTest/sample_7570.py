 walking_distance_premise = 45
walking_distance_hypothesis = 35

# the hypothesis talks about the distance between Fred and Sam, which is also mentioned in the premise
if walking_distance_hypothesis >= walking_distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an upper limit for the distance between Fred and Sam
    # any distance less than 'walking_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

