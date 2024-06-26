gift_premise = 3
gift_hypothesis = 3

# the hypothesis talks about the number of purses given as gift, which is also mentioned in the premise
if gift_hypothesis <= gift_premise:
    # check if the hypothesis value contradicts the estimate of 'gift_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses given as gift
    # any number of purses greater than 'gift_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
