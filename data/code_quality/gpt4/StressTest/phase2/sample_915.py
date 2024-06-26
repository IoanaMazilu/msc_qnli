toys_premise = 27
toys_hypothesis = 57

# The hypothesis talks about the number of toys Kiran has, which is also mentioned in the premise
if toys_premise >= toys_hypothesis:
    # Check if the premise value contradicts the estimate of less than 'toys_hypothesis'
    label = "contradiction"
else:
    # The premise gives an exact number of toys
    # The hypothesis value is greater than the premise value, and so it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
