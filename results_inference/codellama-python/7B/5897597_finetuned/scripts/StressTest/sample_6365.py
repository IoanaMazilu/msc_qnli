watermelons_premise = 136
watermelons_hypothesis = 136

# the hypothesis refers to the number of watermelons mentioned in the premise
if watermelons_hypothesis >= watermelons_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
