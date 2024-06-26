won_tickets_premise = 49.0
lost_tickets_premise = 6.0
spent_tickets_premise = 25.0
remaining_tickets_hypothesis = 18.0

# the hypothesis refers to the number of remaining tickets, which are also mentioned in the premise
# compute the remaining number of tickets in the premise
remaining_tickets_premise = won_tickets_premise - lost_tickets_premise - spent_tickets_premise
if remaining_tickets_hypothesis!= remaining_tickets_premise:
    # check if the number of remaining tickets in the hypothesis contradicts the number of remaining tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
