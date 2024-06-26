kramer_packing_premise = 20
kramer_packing_hypothesis = 10

# the hypothesis refers to the number of boxes packed per minute
if kramer_packing_premise > kramer_packing_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'kramer_packing_premise'
    label = "contradiction"
elif kramer_packing_hypothesis == kramer_packing_premise:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of boxes packed per minute
    # any number of boxes packed per minute less than 'kramer_packing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
