# Premise: Matt and Peter can do together a piece of work in 20 days.
# Hypothesis: Matt and Peter can do together a piece of work in more than 20 days.
# Golden Label: contradiction

work_days_premise = 20
work_days_hypothesis = 20

# the hypothesis refers to the same work duration as in the premise
if work_days_hypothesis > work_days_premise:
    # check if the duration in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # check if the duration in the hypothesis is exactly the same as the one mentioned in the premise
    label = "entailment"
else:
    # if the duration in the hypothesis is less than the one in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

