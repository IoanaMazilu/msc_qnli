# Premise: Sam bought 50 candles and 3 lighters costing 2 dollars each.
# Hypothesis: Sam bought less than 60 candles and 3 lighters costing 2 dollars each.
# Golden Label: entailment

candles_premise = 50
candles_hypothesis = 60
lighters_premise = 3
lighters_hypothesis = 3
lighter_cost_premise = 2
lighter_cost_hypothesis = 2

# the hypothesis refers to the number of bought candles and lighters mentioned in the premise
if candles_premise >= candles_hypothesis:
    # check if the estimate of 'candles_hypothesis' contradicts the number of candle purchases in the premise
    label = "contradiction"
elif lighters_hypothesis != lighters_premise:
    # check if the number of bought lighters in the hypothesis contradicts the number of bought lighters reported in the premise
    label = "contradiction"
elif lighter_cost_hypothesis != lighter_cost_premise:
    # check if the cost of the lighters in the hypothesis contradicts the cost of lighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

