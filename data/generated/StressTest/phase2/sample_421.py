# Premise: Guna has more than 2 flavors of ice cream in him parlor.
# Hypothesis: Guna has 8 flavors of ice cream in him parlor.
# Golden Label: neutral

flavors_premise = 2
flavors_hypothesis = 8

# the hypothesis specifies the number of ice cream flavors at Guna's parlor, as mentioned in the premise
if flavors_hypothesis <= flavors_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'flavors_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of flavors
    # any number of flavors greater than 'flavors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

