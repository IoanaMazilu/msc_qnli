# Premise: Mary works in a restaurant a maximum of 50 hours.
# Hypothesis: Mary works in a restaurant a maximum of 40 hours.
# Golden Label: contradiction

work_hours_premise = 50
work_hours_hypothesis = 40

# the hypothesis refers to the maximum hours Mary works in a restaurant, as stated in the premise
if work_hours_hypothesis > work_hours_premise:
    # check if the maximum working hours in the hypothesis contradicts the maximum hours given in the premise
    label = "contradiction"
elif work_hours_hypothesis == work_hours_premise:
    # if the maximum hours in the hypothesis is equal to the maximum hours in the premise, it's entailment
    label = "entailment"
else:
    # if the maximum hours in the hypothesis is less than the maximum hours in the premise, it's neutral
    label = "neutral"

print(label)

