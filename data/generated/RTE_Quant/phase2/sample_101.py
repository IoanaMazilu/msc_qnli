# Premise: For all last year, business spending on equipment and software grew 13.4 %, the largest increase since 1997.
# Hypothesis: Business spending on equipment and software grew by 13.4 percent.
# Golden Label: entailment

business_spending_growth_premise = 13.4
business_spending_growth_hypothesis = 13.4

# the hypothesis talks about the business spending growth which is also mentioned in the premise
if business_spending_growth_hypothesis != business_spending_growth_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the hypothesis growth rate does not contradict the premise growth rate, we can infer entailment
    label = "entailment"

print(label)

