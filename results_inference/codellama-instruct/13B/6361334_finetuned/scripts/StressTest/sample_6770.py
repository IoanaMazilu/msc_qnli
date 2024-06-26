ration_premise = 6600
ration_hypothesis = 6600

# the hypothesis refers to the number of items among John, Jose & Binoy in the ration 2:4:6
if ration_hypothesis >= ration_premise:
    # check if the hypothesis value contradicts the number of items in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of items
    # any number of items less than 'ration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
