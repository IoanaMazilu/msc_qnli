parents_amount_premise = 60000  # premise: amount owed to parents
parents_amount_hypothesis = 40000  # hypothesis: amount owed to parents after 4 years of college
monthly_payment_premise = 0.06 * 60000  # premise: monthly payment to parents
monthly_payment_hypothesis = 0.04 * 40000  # hypothesis: monthly payment to parents

# first, extract the numerical values from the premise and hypothesis
if parents_amount_premise <= parents_amount_hypothesis:
    # check if the estimate of 'parents_amount_hypothesis' contradicts the amount owed to parents in the premise
    label = "contradiction"
elif monthly_payment_hypothesis!= monthly_payment_premise:
    # check if the monthly payment in the hypothesis contradicts the monthly payment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
