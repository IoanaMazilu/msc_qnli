premise_threshold = 1/4
hypothesis_threshold = 6/4

# the hypothesis refers to the number of top-10-movies lists submitted by the Cinematic Academy's 760 members
if hypothesis_threshold <= premise_threshold:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of top-10-movies lists
    # any number of top-10-movies lists greater than 'premise_threshold' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
