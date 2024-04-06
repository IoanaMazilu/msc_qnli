# Premise: Rupee hits low 65.36/USD, Sensex Falls 300 points, Nifty future trading call on Tuesday 27 Aug, Indian share market tips ~ stocks nifty future call today.
# Hypothesis: Rupee down 68.19/USD, Sensex falls 282.50 points at 17685.58, Today nifty future trading call on Wednesday 28 Aug ~ stocks nifty future call today.
# Golden Label: contradiction

rupee_value_premise = 65.36
rupee_value_hypothesis = 68.19
sensex_points_premise = 300
sensex_points_hypothesis = 282.5
date_day_premise = 27
date_day_hypothesis = 28

# the hypothesis and premise mention the rupee value, the points fall in Sensex and the day of the report
if rupee_value_hypothesis <= rupee_value_premise:
    # check if the rupee value in the hypothesis contradicts the rupee value in the premise
    label = "contradiction"
elif sensex_points_hypothesis > sensex_points_premise:
    # check if the Sensex points fall in the hypothesis contradicts the Sensex points fall in the premise
    label = "contradiction"
elif date_day_hypothesis != date_day_premise + 1:
    # check if the day in the hypothesis is not the day after the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

