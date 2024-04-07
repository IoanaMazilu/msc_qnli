# Premise: If Albert’s monthly earnings rise by 27 %, he would earn $567.
# Hypothesis: If Albert’s monthly earnings rise by 17 %, he would earn $567.
# Golden Label: contradiction

earnings_rise_percentage_premise = 27
earnings_rise_percentage_hypothesis = 17
earnings_value_premise = 567
earnings_value_hypothesis = 567

# the hypothesis refers to the percentage of Albert's earnings rise and the amount he would earn, which are also mentioned in the premise
if earnings_rise_percentage_hypothesis != earnings_rise_percentage_premise:
    # check if the percentage of earnings rise in the hypothesis contradicts the percentage of earnings rise in the premise
    label = "contradiction"
elif earnings_value_hypothesis != earnings_value_premise:
    # check if the amount of earnings in the hypothesis contradicts the amount of earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

