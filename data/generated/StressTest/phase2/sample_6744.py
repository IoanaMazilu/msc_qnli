# Premise: Flora leaves City A 2 hours after Ed.
# Hypothesis: Flora leaves City A more than 1 hours after Ed.
# Golden Label: entailment

flora_leave_time_premise = 2
flora_leave_time_hypothesis = 1

# The hypothesis refers to the time Flora leaves City A after Ed mentioned in the premise
if flora_leave_time_hypothesis >= flora_leave_time_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the time mentioned in the hypothesis is less than the premise, it is entailed
    label = "entailment"

print(label)

