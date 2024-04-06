# Premise: The latest congressional action authorizes $1 million in additional funding to'' provide for a swift completion'' of the U.S. Department of Agriculture's probe into the Rancho Feeding Corporation.
# Hypothesis: The House OKs $1 million for a USDA investigation of a California slaughterhouse.
# Golden Label: entailment

funding_premise = 1000000
funding_hypothesis = 1000000

# the hypothesis mentions the funding amount for a USDA investigation, which is also mentioned in the premise
# however, the hypothesis does not specify the purpose of the investigation or the company being investigated
if funding_hypothesis != funding_premise:
    # check if the funding amount in the hypothesis contradicts the funding amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, it's not a contradiction. But it's also not an entailment since it lacks some details from the premise
    label = "neutral"

print(label)

