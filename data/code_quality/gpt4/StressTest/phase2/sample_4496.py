work_time_renu_premise = 6
work_time_renu_suma_premise = 4
work_time_renu_hypothesis = 4
work_time_renu_suma_hypothesis = 4

# the hypothesis talks about the amount of time Renu and Renu+Suma need to do a piece of work, referenced also in the premise
if work_time_renu_premise != work_time_renu_hypothesis:
    # check if the time estimate for Renu in the hypothesis contradicts the time estimate for Renu in the premise
    label = "contradiction"
elif work_time_renu_suma_premise != work_time_renu_suma_hypothesis:
    # check if the time estimate for Renu and Suma in the hypothesis contradicts the time estimate for Renu and Suma in the premise
    label = "contradiction"
else:
    # if the time estimates in the hypothesis do not contradict the time estimates in the premise, we can infer entailment
    label = "entailment"

print(label)
