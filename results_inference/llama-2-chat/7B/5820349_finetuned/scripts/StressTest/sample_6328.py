boxes_packed_premise = 20
boxes_packed_hypothesis = 10

# the hypothesis refers to the number of boxes Kramer can pack per minute, which is also mentioned in the premise
if boxes_packed_hypothesis >= boxes_packed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_packed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes Kramer can pack
    # any number of boxes less than 'boxes_packed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
