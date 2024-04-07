# Premise: If Albert’s monthly earnings rise by 30 %, he would earn $598.
# Hypothesis: If Albert’s monthly earnings rise by 50 %, he would earn $598.
# Golden Label: contradiction

earnings_increase_premise = 30
earnings_increase_hypothesis = 50
earnings_value_premise = 598
earnings_value_hypothesis = 598

# the hypothesis talks about the percentage increase of Albert's monthly earnings and the resulting amount, both mentioned in the premise
if earnings_increase_premise != earnings_increase_hypothesis and earnings_value_premise == earnings_value_hypothesis:
    # check if the percentage increase value in the hypothesis contradicts the percentage increase in the premise,
    # while the resulting earnings value in the hypothesis is the same as in the premise
    label = "contradiction"
else:
    # any other combination of percentage increase and earnings value in the hypothesis would not contradict the premise values, 
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

