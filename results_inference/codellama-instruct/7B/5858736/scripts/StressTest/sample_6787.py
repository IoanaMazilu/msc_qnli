# define variables for the numerical entities in the premise and hypothesis
premise_total_hours = 21
premise_paid_amount = 1
hypothesis_total_hours = 41
hypothesis_paid_amount = 1

# check if the hypothesis values contradict the premise ones
if hypothesis_total_hours <= premise_total_hours:
    # check if the estimate of 'hypothesis_total_hours' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hypothesis_paid_amount!= premise_paid_amount:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
