# Premise: Zimmer has less than 837 papers to hand out to his class.
# Hypothesis: Zimmer has 237 papers to hand out to his class.
# Golden Label: neutral

papers_premise = 837
papers_hypothesis = 237

# the hypothesis refers to the number of papers Zimmer has to hand out, also mentioned in the premise
if papers_hypothesis >= papers_premise:
    # check if the number of papers in the hypothesis contradicts the estimate of less than 'papers_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of papers
    # any number of papers less than 'papers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

