premise_share_tony = 6500
hypothesis_share_tony = 4500

# the hypothesis refers to the share of Tony in the premise
if hypothesis_share_tony < premise_share_tony:
    # check if the estimate of 'hypothesis_share_tony' contradicts the premise
    label = "contradiction"
elif hypothesis_share_tony == premise_share_tony:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the share of Tony
    # any value less than 'premise_share_tony' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
