won_tickets_premise = 49.0
spent_tickets_premise = 25.0
later_won_tickets_premise = 6.0
total_tickets_hypothesis = 28.0

# the hypothesis refers to the number of tickets Cody would have left, which are mentioned in the premise
# compute the total number of tickets Cody would have in the premise
total_tickets_premise = won_tickets_premise - spent_tickets_premise + later_won_tickets_premise
if total_tickets_hypothesis != total_tickets_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
