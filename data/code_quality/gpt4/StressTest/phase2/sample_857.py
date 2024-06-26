second_leg_time_premise = 53
second_leg_time_hypothesis = 83

# the hypothesis talks about the time Ben took to run the second leg of the course, also mentioned in the premise
if second_leg_time_hypothesis != second_leg_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
