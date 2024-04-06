# Premise: Canadian health officials have confirmed three cases of Enterovirus D68 in British Columbia.
# Hypothesis: Canada confirms three cases in British Columbia.
# Golden Label: entailment

cases_premise = 3
cases_hypothesis = 3

# the hypothesis mentions the number of cases confirmed in British Columbia, which is also referenced in the premise
# however, the hypothesis does not specify the disease, which cannot be entailed from the premise
if cases_hypothesis != cases_premise:
    # check if the number of cases in the hypothesis contradicts the number of cases reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)

