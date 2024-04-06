# Premise: Around ten members of the business delegation will come to Burma.
# Hypothesis: He is leading a delegation of 10 business leaders to the country.
# Golden Label: neutral

members_premise = 10
members_hypothesis = 10

# the hypothesis mentions the number of delegation members, which is also referenced in the premise
# however, the hypothesis refers to the person leading the delegation, which cannot be entailed from the premise
label = "neutral"

print(label)

