money_to_john_premise = 85
money_to_john_hypothesis = 95

# the hypothesis refers to the amount of money to be given to John, which is also mentioned in the premise
if money_to_john_hypothesis <= money_to_john_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    # but it does not entail the premise either
    label = "neutral"

print(label)
