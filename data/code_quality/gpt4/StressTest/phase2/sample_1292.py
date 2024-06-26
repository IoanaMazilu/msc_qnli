work_hours_MWF_premise = 8
work_hours_MWF_hypothesis = 8
work_hours_TT_premise = 6
work_hours_TT_hypothesis = 6

# the hypothesis refers to the work hours of Sheila on Monday, Wednesday, Friday, Tuesday, and Thursday mentioned in the premise
if work_hours_MWF_hypothesis <= work_hours_MWF_premise:
    # check if the estimate of 'work_hours_MWF_hypothesis' contradicts the work hours on MWF in the premise
    label = "contradiction"
elif work_hours_TT_hypothesis != work_hours_TT_premise:
    # check if the work hours on TT in the hypothesis contradict the work hours on TT reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
