won_tickets_premise = 49.0
lost_tickets_premise = 6.0
spent_tickets_premise = 25.0
tickets_hypothesis = 18.0

# first, extract all quantities as valid numbers
won_tickets_premise = int(won_tickets_premise)
lost_tickets_premise = int(lost_tickets_premise)
spent_tickets_premise = int(spent_tickets_premise)
tickets_hypothesis = int(tickets_hypothesis)

# next, compare the quantities
if tickets_hypothesis < won_tickets_premise + lost_tickets_premise - spent_tickets_premise:
    # check if the number of tickets left in the hypothesis contradicts the estimate of more than 'won_tickets_premise'
    label = "contradiction"
elif tickets_hypothesis!= won_tickets_premise:
    # check if the number of tickets left in the hypothesis contradicts the number of tickets won in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
