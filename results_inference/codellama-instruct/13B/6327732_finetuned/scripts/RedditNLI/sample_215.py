premise = "U.S Job loss: Worst in 34 years."
hypothesis = "U.S. January Job Losses Worst in 34 Years."

# the hypothesis and premise mention the number of years since the worst job loss in the US
if "34 years" in premise and "34 years" in hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "entailment"
else:
    # the hypothesis mentions the number of years since the worst job loss in the US, but the premise does not
    label = "neutral"

print(label)
