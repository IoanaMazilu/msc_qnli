less_than_premise = 75
rank_hypothesis = 15

# the hypothesis talks about the rank of a student, referenced also in the premise
if less_than_premise <= rank_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank
    # any rank greater than 'less_than_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
