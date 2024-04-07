# Premise: Catherina works 5 hours per day on Monday, Wednesday and Friday, and 10 hours per day on Tuesday and Thursday.
# Hypothesis: Catherina works more than 2 hours per day on Monday, Wednesday and Friday, and 10 hours per day on Tuesday and Thursday.
# Golden Label: entailment

work_hours_MWF_premise = 5
work_hours_MWF_hypothesis = 2
work_hours_TT_premise = 10
work_hours_TT_hypothesis = 10

# the hypothesis refers to the number of working hours of Catherina on MWF and TT mentioned in the premise
if work_hours_MWF_premise <= work_hours_MWF_hypothesis:
    # check if the estimate of 'work_hours_MWF_hypothesis' contradicts the number of working hours on MWF in the premise
    label = "contradiction"
elif work_hours_TT_hypothesis != work_hours_TT_premise:
    # check if the number of working hours on TT in the hypothesis contradicts the number of working hours on TT reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

