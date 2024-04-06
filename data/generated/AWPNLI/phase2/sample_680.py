# Premise: At the arcade Cody won 49.0 tickets, and he lost 6.0 tickets and later spent 25.0 tickets on a beanie.
# Hypothesis: He would have 18.0 tickets left.
# Golden Label: entailment

won_tickets_premise = 49.0
lost_tickets_premise = 6.0
spent_tickets_premise = 25.0
remaining_tickets_hypothesis = 18.0

# the hypothesis is about the number of tickets left, which is also mentioned in the premise
# compute the total number of tickets left in the premise
remaining_tickets_premise = won_tickets_premise - lost_tickets_premise - spent_tickets_premise
if remaining_tickets_hypothesis != remaining_tickets_premise:
    # check if the number of tickets left in the hypothesis contradicts the number of tickets left from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

