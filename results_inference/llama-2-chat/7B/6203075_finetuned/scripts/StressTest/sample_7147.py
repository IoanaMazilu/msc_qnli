number_premise = 8
number_hypothesis = 4

# the hypothesis refers to the number Cindy is thinking of, which is also mentioned in the premise
if number_hypothesis >= number_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif number_hypothesis < number_premise:
    # if the hypothesis value is less than the premise value, it can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value is exactly equal to the premise value, it is neutral
    label = "neutral"

print(label)
