companies_premise = 9
companies_hypothesis = 9

# the hypothesis mentions the number of companies from UAE in the MSCI index, which is also mentioned in the premise
if companies_hypothesis != companies_premise:
    # check if the number of companies in the hypothesis contradicts the number of companies reported in the premise
    label = "contradiction"
else:
    # if the number of companies in the hypothesis does not contradict the number of companies in the premise, we can infer entailment
    label = "entailment"

print(label)
