candles_bought_premise = 60
candles_bought_hypothesis = 50
lighters_bought_premise = 3
lighters_bought_hypothesis = 3
lighter_cost_premise = 2
lighter_cost_hypothesis = 2

# the hypothesis refers to the number of candles and lighters bought and their cost, mentioned in the premise
if candles_bought_hypothesis >= candles_bought_premise:
    # check if the number of candles bought stated in the hypothesis contradicts the premise estimate of less than 'candles_bought_premise'
    label = "contradiction"
elif lighters_bought_hypothesis != lighters_bought_premise or lighter_cost_hypothesis != lighter_cost_premise:
    # check if the number of lighters bought or their cost in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
