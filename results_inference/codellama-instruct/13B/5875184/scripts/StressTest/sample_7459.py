premise = "To be considered for “ movie of the year, ” a film must appear in at least less than 2/4 of the top-10-movies lists submitted by the Cinematic Academy’s 770 members."
hypothesis = "To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 770 members."

# extract the numerical entities from the premise and hypothesis
premise_threshold = float(premise.split("less than")[1].split("of")[0])
hypothesis_threshold = float(hypothesis.split("at least")[1].split("of")[0])

# check if the hypothesis threshold contradicts the premise threshold
if hypothesis_threshold <= premise_threshold:
    label = "contradiction"
else:
    label = "neutral"

print(label)
