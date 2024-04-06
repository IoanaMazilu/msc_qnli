# Premise: The number of suspected cases in Guinea has grown to 157, with 101 deaths.
# Hypothesis: Mali says it has three suspected Ebola cases.
# Golden Label: neutral

suspected_cases_guinea_premise = 157
deaths_guinea_premise = 101
suspected_cases_mali_hypothesis = 3

# the hypothesis introduces information about suspected cases in Mali, which is not mentioned at all in the premise about Guinea
# there is no shared information between the two sentences that could be compared 
# hence, neither contradiction nor entailment can be inferred
label = "neutral"

print(label)

