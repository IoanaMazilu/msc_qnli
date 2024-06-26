# variables for premise and hypothesis
premise = 7 / 12
hypothesis = 15 / 12

# compare the values of the variables
if hypothesis > premise:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis < premise:
    # the hypothesis value is less than the premise value, but does not contradict it
    label = "neutral"
else:
    # the hypothesis value is equal to or greater than the premise value, and can be entailed from the premise
    label = "entailment"

print(label)
