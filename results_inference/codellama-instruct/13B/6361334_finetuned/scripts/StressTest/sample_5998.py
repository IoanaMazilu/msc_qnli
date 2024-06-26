premise_threshold = 4/4
hypothesis_threshold = 1/4

# the hypothesis refers to the number of top-10-movies lists submitted by the Cinematic Academy's 760 members
if hypothesis_threshold <= premise_threshold:
    # check if the hypothesis value contradicts the premise threshold
    label = "contradiction"
else:
    # the premise gives a threshold for the number of top-10-movies lists
    # any number of lists greater than or equal to 'premise_threshold' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
