candles_premise = 4
candles_hypothesis = 4
flowers_premise = 9
flowers_hypothesis = 9

# the hypothesis talks about the number of candles and flowers Claudia can choose, referenced also in the premise
if candles_hypothesis != candles_premise:
    # check if the number of candles in the hypothesis contradicts the number of candles mentioned in the premise
    label = "contradiction"
elif flowers_hypothesis != flowers_premise:
    # check if the number of flowers in the hypothesis contradicts the number of flowers mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)