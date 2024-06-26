don_premise = 18
mass_premise = 29
king_hypothesis = 18

# the hypothesis talks about the coding of KING, referenced also in the premise
if don_premise <= king_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'don_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the coding of KING
    # any coding of KING less than 'don_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
