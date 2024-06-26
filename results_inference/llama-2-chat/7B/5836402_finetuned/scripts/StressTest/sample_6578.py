shirts_bought_premise = 160
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts bought, which is also referenced in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_bought_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, it does not contradict it, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
