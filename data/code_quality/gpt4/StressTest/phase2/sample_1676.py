candles_bought_premise = 50
candles_bought_hypothesis = 80
lighters_bought_premise = 3
lighters_bought_hypothesis = 3
lighter_cost_premise = 2
lighter_cost_hypothesis = 2

# the hypothesis refers to the number of candles and lighters bought and the cost of lighters, all mentioned in the premise
if candles_bought_hypothesis != candles_bought_premise:
    # check if the number of candles bought in the hypothesis contradicts the number of candles bought reported in the premise
    label = "contradiction"
elif lighters_bought_hypothesis != lighters_bought_premise:
    # check if the number of lighters bought in the hypothesis contradicts the number of lighters bought reported in the premise
    label = "contradiction"
elif lighter_cost_hypothesis != lighter_cost_premise:
    # check if the cost of lighters in the hypothesis contradicts the cost of lighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
