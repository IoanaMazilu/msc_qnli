work_hours_premise = 80
work_hours_hypothesis = 10

# The hypothesis refers to the number of work hours per day mentioned in the premise
if work_hours_hypothesis == work_hours_premise:
    # If the work hours in the hypothesis equal the work hours in the premise, we can infer entailment
    label = "entailment"
elif work_hours_hypothesis > work_hours_premise:
    # If the work hours in the hypothesis are more than the work hours in the premise, it contradicts the premise
    label = "contradiction"
else:
    # If the work hours in the hypothesis are less than the work hours in the premise, it does not contradict the premise, but cannot be fully entailed from it either
    label = "neutral"

print(label)
