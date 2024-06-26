tickets_won_premise = 49.0
tickets_lost_premise = 6.0
tickets_spent_premise = 25.0
tickets_left_hypothesis = 18.0

# the hypothesis refers to the number of tickets left, which are also mentioned in the premise
# compute the total number of tickets in the premise
total_tickets_premise = tickets_won_premise - tickets_lost_premise - tickets_spent_premise
if tickets_left_hypothesis!= total_tickets_premise:
    # check if the number of tickets left in the hypothesis contradicts the number of tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
