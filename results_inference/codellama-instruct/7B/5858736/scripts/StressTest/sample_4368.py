# Define variables for the numerical entities in the premise and hypothesis
premise_total_hours = 41
premise_paid_amount = 1
hypothesis_total_hours = 51
hypothesis_paid_amount = 1

# Calculate the number of hours worked by Harry
harry_total_hours = premise_total_hours - hypothesis_total_hours

# Check if the hypothesis values contradict the premise
if harry_total_hours < 0:
    label = "contradiction"
elif harry_total_hours % premise_paid_amount!= 0:
    label = "contradiction"
else:
    label = "entailment"

print(label)
