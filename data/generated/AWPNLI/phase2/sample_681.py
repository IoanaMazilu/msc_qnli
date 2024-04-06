# Premise: At the arcade Cody won 49.0 tickets, and he lost 6.0 tickets and later spent 25.0 tickets on a beanie.
# Hypothesis: He would have 21.0 tickets left.
# Golden Label: contradiction

won_tickets_premise = 49.0
lost_tickets_premise = 6.0
spent_tickets_premise = 25.0
left_tickets_hypothesis = 21.0

# the hypothesis refers to the number of tickets left, which can be calculated using the information in the premise
# compute the total number of tickets left in the premise
left_tickets_premise = won_tickets_premise - lost_tickets_premise - spent_tickets_premise
if left_tickets_hypothesis != left_tickets_premise:
    # check if the number of tickets left in the hypothesis contradicts the number of tickets left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
