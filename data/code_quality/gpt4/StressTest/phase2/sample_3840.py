work_hours_MWF_premise = 10
work_hours_MWF_hypothesis = 50
work_hours_TT_premise = 15
work_hours_TT_hypothesis = 15

# the hypothesis talks about the number of work hours per day on MWF and TT, which are also mentioned in the premise
if work_hours_MWF_hypothesis >= work_hours_MWF_premise:
    # check if the estimate of 'work_hours_MWF_hypothesis' contradicts the number of hours worked on MWF in the premise
    label = "contradiction"
elif work_hours_TT_hypothesis != work_hours_TT_premise:
    # check if the number of hours worked on TT in the hypothesis contradicts the number of hours worked on TT in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
