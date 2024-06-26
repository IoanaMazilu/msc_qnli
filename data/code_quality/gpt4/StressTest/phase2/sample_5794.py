candles_premise = 4
flowers_premise = 4
candles_hypothesis = 4
flowers_hypothesis = 8

# the hypothesis refers to the number of candles and flowers Klaudia can choose for the arrangement, mentioned also in the premise
if candles_hypothesis != candles_premise:
    # check if the number of candles in the hypothesis contradicts the number of candles mentioned in the premise
    label = "contradiction"
elif flowers_hypothesis <= flowers_premise:
    # check if the number of flowers in the hypothesis contradicts the estimate of more than 'flowers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flowers
    # any number of flowers greater than 'flowers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
