# Premise: Mary works in a restaurant a maximum of more than 10 hours.
# Hypothesis: Mary works in a restaurant a maximum of 60 hours.
# Golden Label: neutral

max_hours_worked_premise = 10
max_hours_worked_hypothesis = 60

# the hypothesis refers to the maximum number of hours Mary works in a restaurant, which is also mentioned in the premise
if max_hours_worked_hypothesis <= max_hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'max_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the maximum number of hours Mary works
    # any number of hours greater than 'max_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

