# Premise: Chris has worked with more than 100,000 golfers throughout his career.
# Hypothesis: He has personally coached more than 100,000 golfers.
# Golden Label: entailment

golfers_premise = 100000
golfers_hypothesis = 100000

# the hypothesis mentions the number of golfers coached, which is also mentioned in the premise
# however, the hypothesis specifies "personally coached" which cannot be entailed from the premise
label = "neutral"

print(label)

