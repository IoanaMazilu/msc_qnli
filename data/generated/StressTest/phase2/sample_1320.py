# Premise: Zimmer has 237 papers to hand out to his class.
# Hypothesis: Zimmer has less than 837 papers to hand out to his class.
# Golden Label: entailment

papers_premise = 237
papers_hypothesis = 837

# the hypothesis talks about the number of papers Zimmer has, referenced also in the premise
if papers_premise >= papers_hypothesis:
    # check if the premise value contradicts the estimate of less than 'papers_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the number of papers
    # any number of papers less than 'papers_hypothesis' is consistent with the hypothesis, and can be explicitly entailed from the premise
    label = "entailment"

print(label)

