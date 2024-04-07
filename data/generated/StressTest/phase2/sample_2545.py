# Premise: If Albert’s monthly earnings rise by less than 30 %, he would earn $560.
# Hypothesis: If Albert’s monthly earnings rise by 20 %, he would earn $560.
# Golden Label: neutral

earnings_increase_premise = 30
earnings_increase_hypothesis = 20
earnings_premise = 560
earnings_hypothesis = 560

# the hypothesis talks about the increase in Albert's earnings and the final amount
if earnings_increase_hypothesis >= earnings_increase_premise:
    # if the increase in earnings suggested by the hypothesis contradicts the premise
    label = "contradiction"
elif earnings_hypothesis != earnings_premise:
    # if the final earnings amount in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

