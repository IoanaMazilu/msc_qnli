james_work_hours_premise = 41
james_work_hours_hypothesis = 51

# the hypothesis is about the number of hours James worked last week, which is also mentioned in the premise
if james_work_hours_hypothesis <= james_work_hours_premise:
    # the hypothesis suggests that James worked less than 51 hours last week
    # if this value is less than or equal to the hours claimed in the premise, it is a contradiction
    label = "contradiction"
elif james_work_hours_hypothesis > james_work_hours_premise:
    # the hypothesis suggests that James worked less than 51 hours last week
    # if this value is greater than the hours claimed in the premise, it is an entailment
    label = "entailment"

print(label)
