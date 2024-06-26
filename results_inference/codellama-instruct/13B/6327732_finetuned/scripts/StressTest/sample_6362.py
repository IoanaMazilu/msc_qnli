watermelons_premise = 200
watermelons_hypothesis = 100

# the hypothesis refers to the number of watermelons mentioned in the premise
if watermelons_hypothesis <= watermelons_premise:
    # check if the estimate of 'watermelons_hypothesis' contradicts the number of watermelons in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of watermelons
    # any number of watermelons greater than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
