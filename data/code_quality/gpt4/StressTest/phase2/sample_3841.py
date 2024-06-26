hours_worked_MWF_premise = 50
hours_worked_MWF_hypothesis = 10
hours_worked_TT_premise = 15
hours_worked_TT_hypothesis = 15

# the hypothesis refers to the number of hours Diana works on specific days of the week, which is also mentioned in the premise
if hours_worked_MWF_hypothesis >= hours_worked_MWF_premise:
    # check if the number of hours worked on MWF in the hypothesis contradicts the premise
    label = "contradiction"
elif hours_worked_TT_hypothesis != hours_worked_TT_premise:
    # check if the number of hours worked on TT in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hours worked on both sets of days in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
