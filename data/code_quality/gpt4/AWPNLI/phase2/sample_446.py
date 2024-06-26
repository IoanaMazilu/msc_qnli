gate_tickets_premise = 9570.0
online_tickets_premise = 3867.0
total_tickets_hypothesis = 13437.0

# the hypothesis refers to the total number of tickets sold, which are also mentioned in the premise
# compute the total number of tickets sold in the premise
total_tickets_premise = gate_tickets_premise + online_tickets_premise

if total_tickets_hypothesis != total_tickets_premise:
    # check if the total number of tickets in the hypothesis contradicts the total number of tickets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
