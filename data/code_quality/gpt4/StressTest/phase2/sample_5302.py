hours_worked_MWF_premise = 80
hours_worked_MWF_hypothesis = 10
hours_worked_TT_premise = 8
hours_worked_TT_hypothesis = 8

# The hypothesis refers to the hours Sharmila works on Monday, Wednesday, Friday, Tuesday and Thursday as mentioned in the premise
if hours_worked_MWF_hypothesis >= hours_worked_MWF_premise:
    # check if the hours worked on Monday, Wednesday and Friday in the hypothesis contradicts the premise
    label = "contradiction"
elif hours_worked_TT_hypothesis != hours_worked_TT_premise:
    # check if the hours worked on Tuesday and Thursday in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
