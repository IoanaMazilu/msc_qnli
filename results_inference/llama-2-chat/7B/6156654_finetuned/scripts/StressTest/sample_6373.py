pencils_premise = 425
pencils_hypothesis = 125

# the hypothesis talks about the number of pencils Shreehari has, which is also mentioned in the premise
if pencils_hypothesis >= pencils_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif pencils_hypothesis < pencils_premise:
    # check if the hypothesis value is less than the premise value, which means the hypothesis entails the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
