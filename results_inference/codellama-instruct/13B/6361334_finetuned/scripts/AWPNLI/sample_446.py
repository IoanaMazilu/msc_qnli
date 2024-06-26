sold_tickets_premise = 9570.0
sold_tickets_online_premise = 3867.0
total_sold_tickets_hypothesis = 13437.0

# the hypothesis refers to the total number of tickets sold, which are also mentioned in the premise
# compute the total number of tickets sold from the premise
total_sold_tickets_premise = sold_tickets_premise + sold_tickets_online_premise
if total_sold_tickets_hypothesis!= total_sold_tickets_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
