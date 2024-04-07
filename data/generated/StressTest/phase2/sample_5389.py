# Premise: If Albert’s monthly earnings rise by less than 74 %, he would earn $678.
# Hypothesis: If Albert’s monthly earnings rise by 14 %, he would earn $678.
# Golden Label: neutral

earnings_increase_premise = 74
earnings_increase_hypothesis = 14
earnings_premise = 678
earnings_hypothesis = 678

# the hypothesis refers to Albert's monthly earnings and the percentage increase in his earnings
if earnings_increase_hypothesis >= earnings_increase_premise:
    # check if the percentage increase in earnings specified in the hypothesis contradicts the premise
    label = "contradiction"
elif earnings_hypothesis != earnings_premise:
    # check if the earnings value in the hypothesis contradicts the earnings value in the premise
    label = "contradiction"
else:
    # the percentage increase in the hypothesis is less than the premise and the earnings value is the same
    # this means the hypothesis does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

