number_premise = 4
number_hypothesis = 8

# the hypothesis talks about the number Cindy is thinking of, referenced also in the premise
if number_hypothesis < number_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif number_hypothesis > number_premise:
    # check if the hypothesis value is greater than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it's neutral
    label = "neutral"

print(label)
