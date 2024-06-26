# define variables with representative names for the numerical entities in both inputs
total_hours_last_week_premise = 11
total_hours_last_week_hypothesis = 41

# extract all quantities as valid numbers (integers or floats)
total_hours_last_week_premise = int(total_hours_last_week_premise)
total_hours_last_week_hypothesis = int(total_hours_last_week_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if total_hours_last_week_hypothesis <= total_hours_last_week_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_hours_last_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked last week
    # any number of hours greater than 'total_hours_last_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
