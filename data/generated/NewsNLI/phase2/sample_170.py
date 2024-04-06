# Premise: If the driver beats the ticket, they pay Fixed 25% of what the citation would have cost.
# Hypothesis: If Fixed gets someone out of a ticket, it charges them 25% of the ticket fine.
# Golden Label: entailment

cost_percentage_premise = 0.25
cost_percentage_hypothesis = 0.25

# the hypothesis mentions the percentage of the ticket cost charged by Fixed, which is also mentioned in the premise
if cost_percentage_hypothesis != cost_percentage_premise:
    # check if the percentage cost in the hypothesis contradicts the percentage cost reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

