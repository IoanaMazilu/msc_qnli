max_hours_worked_premise = 30
max_hours_worked_hypothesis = 40

# the hypothesis talks about the maximum hours Mary works in a restaurant, referenced also in the premise
if max_hours_worked_hypothesis <= max_hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'max_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the maximum hours Mary works
    # any number of hours greater than 'max_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)