less_than_60_pairs_premise = 60
less_than_60_pairs_hypothesis = 20

# the hypothesis talks about the number of pairs of matched gloves owned by Andy
if less_than_60_pairs_hypothesis <= less_than_60_pairs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_60_pairs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched gloves
    # any number of pairs of matched gloves greater than 'less_than_60_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
