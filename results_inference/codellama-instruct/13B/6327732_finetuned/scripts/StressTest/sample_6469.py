carpet_area_premise = 0.3
carpet_area_hypothesis = 0.2

# the hypothesis refers to the percentage of the living room floor covered by a carpet
if carpet_area_hypothesis <= carpet_area_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carpet_area_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the living room floor covered by a carpet
    # any percentage greater than 'carpet_area_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
