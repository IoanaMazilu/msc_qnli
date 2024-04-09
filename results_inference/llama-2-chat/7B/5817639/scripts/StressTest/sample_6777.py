percentage_premise = 60
percentage_hypothesis = 40

# the hypothesis refers to the percentage scores of Bright, Bivi, and Lisa in the premise
if percentage_hypothesis <= percentage_premise:
    # check if the hypothesis value contradicts the estimate of Bright's percentage in the premise
    label = "contradiction"
elif percentage_hypothesis - percentage_premise == 20:
    # check if the hypothesis value is consistent with the estimate of Bright's percentage in the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value contradicts the estimate of Bright's percentage in the premise
    label = "contradiction"

print(label)
