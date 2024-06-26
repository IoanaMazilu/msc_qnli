# define variables with representative names for the numerical entities in both inputs
earnings_last_week_premise = 210
hours_worked_premise = 0
earnings_last_week_hypothesis = 0
hours_worked_hypothesis = 0

# extract all quantities as valid numbers (integers or floats)
earnings_last_week_premise = float(earnings_last_week_premise)
hours_worked_premise = float(hours_worked_premise)
earnings_last_week_hypothesis = float(earnings_last_week_hypothesis)
hours_worked_hypothesis = float(hours_worked_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if earnings_last_week_hypothesis > earnings_last_week_premise:
    # check if the hypothesis value contradicts the estimate of 'earnings_last_week_premise'
    label = "contradiction"
elif hours_worked_hypothesis!= hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
