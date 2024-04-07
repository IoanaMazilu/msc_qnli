# Premise: Mary works in a restaurant a maximum of 45 hours.
# Hypothesis: Mary works in a restaurant a maximum of 35 hours.
# Golden Label: contradiction

max_work_hours_premise = 45
max_work_hours_hypothesis = 35

# the hypothesis talks about the maximum hours Mary works in a restaurant, also referenced in the premise
if max_work_hours_hypothesis > max_work_hours_premise:
    # check if the hypothesis value contradicts the maximum hours of 'max_work_hours_premise'
    label = "contradiction"
elif max_work_hours_hypothesis == max_work_hours_premise:
    # the premise gives an exact maximum number of work hours
    # if the maximum number of work hours in the hypothesis matches the premise, we can infer entailment
    label = "entailment"
else:
    # any maximum number of work hours less than 'max_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

