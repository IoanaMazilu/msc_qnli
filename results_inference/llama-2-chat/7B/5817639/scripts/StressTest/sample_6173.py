tip_premise = 0.15  # 15% tip over original price
tip_hypothesis = 0.25  # 25% tip over original price

# the hypothesis talks about the tip paid by John and Jane
if tip_hypothesis <= tip_premise:
    # check if the hypothesis value contradicts the estimate of the tip paid by John in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the tip paid by John, while the hypothesis gives a different estimate
    label = "neutral"

print(label)
