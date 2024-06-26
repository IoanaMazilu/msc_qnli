carpet_area_premise = 30
carpet_area_hypothesis = 20

# the hypothesis refers to the percentage of the living room floor covered by a carpet, mentioned in the premise
if carpet_area_hypothesis <= carpet_area_premise:
    # check if the estimate of 'carpet_area_hypothesis' contradicts the percentage of the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the living room floor covered by a carpet
    # any percentage greater than 'carpet_area_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
