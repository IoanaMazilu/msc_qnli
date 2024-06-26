height_difference_premise = 356
height_difference_hypothesis = 556

# the hypothesis refers to the height difference between the two buildings mentioned in the premise
if height_difference_hypothesis <= height_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'height_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the height difference
    # any height difference greater than 'height_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
