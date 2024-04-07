# Premise: Mary works in a restaurant a maximum of more than 60 hours.
# Hypothesis: Mary works in a restaurant a maximum of 80 hours.
# Golden Label: neutral

max_work_hours_premise = 60
max_work_hours_hypothesis = 80

# the hypothesis talks about the maximum number of hours Mary works in a restaurant, referenced also in the premise
if max_work_hours_hypothesis <= max_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'max_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the maximum work hours
    # any number of hours greater than 'max_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

