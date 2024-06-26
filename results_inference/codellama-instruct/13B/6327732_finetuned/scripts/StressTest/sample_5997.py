premise_threshold = 1/4
hypothesis_threshold = 4/4

# the hypothesis talks about the number of top-10-movies lists in which a film must appear
# the premise mentions the number of top-10-movies lists in which a film must appear
if hypothesis_threshold <= premise_threshold:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the number of top-10-movies lists in which a film must appear
    # any number of top-10-movies lists greater than 'premise_threshold' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
