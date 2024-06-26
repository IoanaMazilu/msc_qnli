candles_choice_premise = 2
candles_choice_hypothesis = 2
flowers_choice_premise = 8
flowers_choice_hypothesis = 4

# the hypothesis refers to the number of candles and flowers Klaudia can choose, mentioned in the premise
if candles_choice_hypothesis != candles_choice_premise:
    # check if the number of candles Klaudia can choose in the hypothesis contradicts the number of candles she can choose in the premise
    label = "contradiction"
elif flowers_choice_hypothesis >= flowers_choice_premise:
    # check if the number of flowers Klaudia can choose in the hypothesis contradicts the number of flowers she can choose in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
