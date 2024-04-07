# Premise: If Albert’s monthly earnings rise by less than 40 %, he would earn $598.
# Hypothesis: If Albert’s monthly earnings rise by 30 %, he would earn $598.
# Golden Label: neutral

earnings_rise_premise = 40
earnings_rise_hypothesis = 30
earnings_result_premise = 598
earnings_result_hypothesis = 598

# the hypothesis refers to the percentage of Albert's earnings rise and the resulting earnings, 
# both mentioned in the premise
if earnings_rise_premise < earnings_rise_hypothesis:
    # check if the percentage of 'earnings_rise_hypothesis' contradicts the percentage rise in the premise
    label = "contradiction"
elif earnings_result_hypothesis != earnings_result_premise:
    # check if the resulting earnings in the hypothesis contradicts the resulting earnings reported in the premise
    label = "contradiction"
elif earnings_rise_premise > earnings_rise_hypothesis and earnings_result_hypothesis == earnings_result_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # any other scenario would indicate neutrality
    label = "neutral"

print(label)

