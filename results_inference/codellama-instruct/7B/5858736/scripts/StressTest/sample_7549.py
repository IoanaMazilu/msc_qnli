saving_amount_premise = 80
saving_amount_hypothesis = 30
loan_payment_premise = 80
loan_payment_hypothesis = 30
current_balance_premise = 80
current_balance_hypothesis = 30

# the hypothesis refers to the number of saved amount and loan payment mentioned in the premise
if saving_amount_hypothesis <= saving_amount_premise:
    # check if the estimate of'saving_amount_hypothesis' contradicts the number of saved amount in the premise
    label = "contradiction"
elif loan_payment_hypothesis!= loan_payment_premise:
    # check if the number of loan payment in the hypothesis contradicts the number of loan payment reported in the premise
    label = "contradiction"
elif current_balance_hypothesis!= current_balance_premise:
    # check if the number of current balance in the hypothesis contradicts the number of current balance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
