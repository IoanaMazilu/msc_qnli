premise_threshold = 1/4
hypothesis_threshold = 3/4

# the hypothesis refers to the number of top-10-movies lists submitted by the Cinematic Academy's 770 members
if hypothesis_threshold <= premise_threshold:
    # check if the hypothesis value contradicts the estimate of at least 'premise_threshold'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of top-10-movies lists submitted by the Cinematic Academy's 770 members
    # any number of top-10-movies lists greater than 'premise_threshold' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
