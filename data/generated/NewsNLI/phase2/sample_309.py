# Premise: BP has received 3,400 claims for lost income and damages and 295 of those claims have been paid, at a price of $3.5 million, Nagel said.
# Hypothesis: BP hit with 3,400 claims for lost income and damages ; 295 paid, to tune of $3.5 million.
# Golden Label: entailment

claims_received_premise = 3400
claims_received_hypothesis = 3400
claims_paid_premise = 295
claims_paid_hypothesis = 295
total_amount_paid_premise = 3.5e6
total_amount_paid_hypothesis = 3.5e6

# the hypothesis mentions the number of claims received and paid by BP and the total amount paid, which are also mentioned in the premise
if claims_received_hypothesis != claims_received_premise:
    # check if the number of claims received in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif claims_paid_hypothesis != claims_paid_premise:
    # check if the number of claims paid from the hypothesis contradicts the number of claims paid in the premise
    label = "contradiction"
elif total_amount_paid_hypothesis != total_amount_paid_premise:
    # check if the total amount paid from the hypothesis contradicts the total amount paid in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

