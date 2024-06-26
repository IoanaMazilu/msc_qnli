premise = "To be considered for “ movie of the year, ” a film must appear in at least less than 4/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."
hypothesis = "To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."

# extract the numerical entities from the premise and hypothesis
premise_threshold = premise.split("less than")[1].split("of the top-10-movies lists")[0]
hypothesis_threshold = hypothesis.split("at least")[1].split("of the top-10-movies lists")[0]

# compare the thresholds
if premise_threshold > hypothesis_threshold:
    label = "contradiction"
elif premise_threshold == hypothesis_threshold:
    label = "neutral"
else:
    label = "entailment"

print(label)
