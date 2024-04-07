# Premise: Claudia can choose any two of four different candles and any more than 7 of 9 different flowers for a centerpiece arrangement.
# Hypothesis: Claudia can choose any two of four different candles and any 8 of 9 different flowers for a centerpiece arrangement.
# Golden Label: neutral

candles_choice_premise = 2
candles_choice_hypothesis = 2
flowers_choice_premise = 7
flowers_choice_hypothesis = 8

# the hypothesis refers to the number of candles and flowers Claudia can choose for a centerpiece, also mentioned in the premise
if candles_choice_hypothesis != candles_choice_premise:
    # check if the number of candles mentioned in the hypothesis contradicts the number of candles in the premise
    label = "contradiction"
elif flowers_choice_hypothesis <= flowers_choice_premise:
    # check if the number of flowers in the hypothesis contradicts the estimate of more than 'flowers_choice_premise' flowers
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flowers
    # any number of flowers greater than 'flowers_choice_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

