premise = "To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 770 members."
hypothesis = "To be considered for “ movie of the year, ” a film must appear in at least less than 2/4 of the top-10-movies lists submitted by the Cinematic Academy’s 770 members."

# extract the numerical entities from the premise and hypothesis
premise_threshold = 1/4
hypothesis_threshold = 2/4

# compare the thresholds
if premise_threshold <= hypothesis_threshold:
    # the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
