watermelons_premise = 136
watermelons_hypothesis = 536

# the hypothesis refers to the number of watermelons mike had after Sally left
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the number of watermelons in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of watermelons mike had after Sally left
    # any number of watermelons greater than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
