percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6
time_period = 4

# the hypothesis refers to the percentage of the amount given back each month, which is also mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif percentage_given_back_hypothesis < percentage_given_back_premise:
    # if the hypothesis value is less than the premise value, it is entailed by the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
