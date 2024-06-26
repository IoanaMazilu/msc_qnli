total_hours_premise = 1
total_hours_hypothesis = 3

# the hypothesis refers to the total hours of jogging and walking mentioned in the premise
if total_hours_hypothesis <= total_hours_premise:
    # check if the total hours in the hypothesis contradicts the estimate of more than 'total_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total hours
    # any total hours greater than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
