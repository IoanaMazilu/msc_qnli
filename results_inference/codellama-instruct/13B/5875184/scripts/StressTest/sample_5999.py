premise = "To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."
hypothesis = "To be considered for “ movie of the year, ” a film must appear in at least 6/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."

# extract the numerical entities from the premise and hypothesis
premise_threshold = 1/4
hypothesis_threshold = 6/4

# compare the thresholds
if hypothesis_threshold > premise_threshold:
    # the hypothesis threshold is greater than the premise threshold, so the hypothesis is more specific
    label = "entailment"
else:
    # the hypothesis threshold is less than or equal to the premise threshold, so the hypothesis is less specific
    label = "neutral"

print(label)
