suspected_cases_guinea_premise = 157
deaths_guinea_premise = 101
suspected_cases_mali_hypothesis = 3

# the hypothesis introduces information about suspected cases in Mali, which is not mentioned at all in the premise about Guinea
# there is no shared information between the two sentences that could be compared 
# hence, neither contradiction nor entailment can be inferred
label = "neutral"

print(label)
