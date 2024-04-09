funding_premise = 1000000
investigation_premise = "probe"
funding_hypothesis = 1000000
investigation_hypothesis = "investigation"

# the hypothesis mentions the funding amount and the investigation type, which are also mentioned in the premise
# however, the hypothesis refers to a different phase of the investigation, which cannot be entailed from the premise
label = "neutral"

print(label)
