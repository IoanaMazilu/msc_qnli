premise_tickets_gate = 9570.0
premise_tickets_online = 3867.0
total_tickets_premise = premise_tickets_gate + premise_tickets_online

hypothesis_tickets = 13437.0

if total_tickets_premise == hypothesis_tickets:
    label = "entailment"
else:
    label = "contradiction"

print(label)
