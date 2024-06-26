speed_premise = 2
speed_hypothesis = 5
meet_distance = 0

# the hypothesis talks about the speed of Fred and Sam, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed of Sam in the premise
    label = "contradiction"
elif meet_distance == 0:
    # if the distance between their meeting points is 0, then the hypothesis cannot be entailed from the premise
    label = "neutral"
else:
    # the premise gives an estimate for the distance between their meeting points
    # any distance greater than'meet_distance' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
