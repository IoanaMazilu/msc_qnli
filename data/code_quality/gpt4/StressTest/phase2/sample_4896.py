drum_time_premise = 6
drum_time_hypothesis = 7

# the hypothesis talks about the time Zane needs to craft a drum, referenced also in the premise
if drum_time_hypothesis < drum_time_premise:
    # check if the hypothesis value contradicts the exact time 'drum_time_premise' given in the premise
    label = "contradiction"
elif drum_time_hypothesis > drum_time_premise:
    # the premise gives an exact time for making a drum
    # any time greater than 'drum_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
