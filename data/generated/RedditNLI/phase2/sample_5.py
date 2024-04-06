# Premise: Indian Rupee down, Tomorrow On Monday stock nifty future trading call 26 Aug, Stocks nifty future call today ~ stocks nifty future call today.
# Hypothesis: SENSEX Nifty up, Today stocks nifty future trading tips and call on Thursday 22 Aug, Nifty top gainers and losers stocks ~ stocks nifty future call today.
# Golden Label: neutral

date_premise = 26
date_hypothesis = 22
day_of_week_premise = "Monday"
day_of_week_hypothesis = "Thursday"

# the hypothesis and premise mention the date and day of the week for the nifty future trading call
if date_premise != date_hypothesis:
    # check if the date in the hypothesis contradicts the date in the premise
    label = "contradiction"
elif day_of_week_premise != day_of_week_hypothesis:
    # check if the day of the week in the hypothesis contradicts the day of the week in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

