premise_won_tickets = 49.0
premise_lost_tickets = 6.0
premise_spent_tickets = 25.0
hypothesis_left_tickets = 18.0

# the hypothesis refers to the number of tickets left, which are also mentioned in the premise
# compute the total number of tickets won and lost from the premise
total_tickets_premise = premise_won_tickets + premise_lost_tickets
# compute the total number of tickets spent from the premise
total_spent_tickets = premise_spent_tickets + premise_lost_tickets
# check if the number of tickets left in the hypothesis contradicts the number of tickets from the premise
if hypothesis_left_tickets!= total_tickets_premise - total_spent_tickets:
    label = "contradiction"
else:
    label = "entailment"

print(label)
