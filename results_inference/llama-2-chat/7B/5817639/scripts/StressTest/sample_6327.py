boxes_packed_premise = 10
boxes_packed_hypothesis = 20

# the hypothesis talks about the number of boxes of cigarettes packed by Kramer, which is also mentioned in the premise
if boxes_packed_premise <= boxes_packed_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'boxes_packed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes packed,
    # any number of boxes packed greater than 'boxes_packed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
