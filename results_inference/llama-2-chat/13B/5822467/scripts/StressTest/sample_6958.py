venkat_toys_premise = 20 * 12 * 275
venkat_toys_hypothesis = 20 * 12 * 375

# the hypothesis talks about the rate of toys purchased, which is also mentioned in the premise
if venkat_toys_hypothesis > venkat_toys_premise:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif venkat_toys_hypothesis == venkat_toys_premise:
    # the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise gives an estimate for the rate of toys purchased
    # any rate greater than the premise rate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
