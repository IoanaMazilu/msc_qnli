# Premise: If Albert’s monthly earnings rise by 36 %, he would earn $495.
# Hypothesis: If Albert’s monthly earnings rise by less than 66 %, he would earn $495.
# Golden Label: entailment

earnings_increase_premise = 36
earnings_hypothesis = 495
earnings_increase_hypothesis = 66

# The hypothesis refers to Albert's earnings increase percentage and his earnings, also mentioned in the premise
if earnings_increase_hypothesis > earnings_increase_premise:
    # check if the hypothesis value contradicts the premise value of 'earnings_increase_premise'
    label = "contradiction"
elif earnings_increase_hypothesis < earnings_increase_premise:
    # check if the hypothesis value contradicts the premise value of 'earnings_increase_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

