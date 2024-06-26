walking_distance_premise = 2
walking_distance_hypothesis = 7
walking_time_premise = 1 + 15
walking_time_hypothesis = 1 + 15

# the hypothesis talks about the distance Jack walked, which is also referenced in the premise
if walking_distance_hypothesis <= walking_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'walking_distance_premise'
    label = "contradiction"
elif walking_time_hypothesis!= walking_time_premise:
    # check if the walking time in the hypothesis contradicts the walking time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'walking_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
