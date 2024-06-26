tickets_sold_premise = 9570.0 + 3867.0
tickets_sold_hypothesis = 13437.0

# the hypothesis refers to the total number of tickets sold, which are also mentioned in the premise
# compute the total number of tickets sold in the premise
total_tickets_sold_premise = tickets_sold_premise + tickets_sold_hypothesis
if total_tickets_sold_premise!= tickets_sold_hypothesis:
    # check if the number of tickets in the hypothesis contradicts the number of tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
