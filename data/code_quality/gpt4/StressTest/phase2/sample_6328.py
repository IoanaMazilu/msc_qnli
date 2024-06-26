boxes_packed_premise = 20
boxes_packed_hypothesis = 10

# the hypothesis talks about the number of boxes that Kramer can pack, referenced also in the premise
if boxes_packed_hypothesis >= boxes_packed_premise:
    # check if the hypothesis value contradicts the premise that Kramer can pack less than 'boxes_packed_premise' per minute
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes packed
    # any number of boxes less than 'boxes_packed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
