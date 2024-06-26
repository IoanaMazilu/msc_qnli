outfit_premise = 1
outfit_hypothesis = 4

# the hypothesis talks about the number of shirts in an outfit, referenced also in the premise
if outfit_hypothesis > outfit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif outfit_hypothesis < outfit_premise:
    # check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"

print(label)
