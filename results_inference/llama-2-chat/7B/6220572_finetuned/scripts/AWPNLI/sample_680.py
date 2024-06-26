won_tickets_premise = 49.0
lost_tickets_premise = 6.0
spent_tickets_premise = 25.0
left_tickets_hypothesis = 18.0

# the hypothesis talks about the number of tickets left, which is also referenced in the premise
# compute the total number of tickets left from the premise
total_left_tickets_premise = won_tickets_premise - lost_tickets_premise - spent_tickets_premise
if total_left_tickets_hypothesis!= total_left_tickets_premise:
    # check if the number of tickets left from the hypothesis contradicts the number of tickets left from the premise
    label = "contradiction"
elif won_tickets_premise - lost_tickets_premise - spent_tickets_premise!= 18.0:
    # check if the number of tickets left from the hypothesis contradicts the number of tickets left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
