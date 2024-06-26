 coffee_deal_premise = 7.2
coffee_deal_hypothesis = 7.15

# the hypothesis mentions the amount of money Nestle will pay to Starbucks in a coffee tie-up, which is also referenced in the premise
if coffee_deal_hypothesis!= coffee_deal_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
