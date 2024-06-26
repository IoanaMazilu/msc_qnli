jog_time_premise = 1
jog_time_hypothesis = 3

# the hypothesis talks about the total jogging time, which is also mentioned in the premise
if jog_time_hypothesis <= jog_time_premise:
    # check if the jogging time in the hypothesis contradicts the premise
    label = "contradiction"
elif jog_time_hypothesis > jog_time_premise:
    # check if the jogging time in the hypothesis is greater than the one in the premise
    # this is a possible situation, so we cannot infer entailment
    label = "neutral"
else:
    # if the jogging time in the hypothesis is greater than the one in the premise, but not contradicting it,
    # we can infer entailment
    label = "entailment"

print(label)
