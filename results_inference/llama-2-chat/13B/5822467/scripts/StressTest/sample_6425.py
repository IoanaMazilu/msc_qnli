marie_account_premise = 248
marie_account_hypothesis = 148

# the hypothesis refers to the amount of money in Marie's account
if marie_account_premise <= marie_account_hypothesis:
    # check if the estimate of'marie_account_hypothesis' contradicts the amount of money in Marie's account reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer neutrality
    label = "neutral"

print(label)
