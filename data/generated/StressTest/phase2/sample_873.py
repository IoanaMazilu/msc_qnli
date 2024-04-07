# Premise: Rathi took a loan for 6 years at the rate of 5% per annum on Simple Interest, If the total interest paid was Rs.
# Hypothesis: Rathi took a loan for more than 5 years at the rate of 5% per annum on Simple Interest, If the total interest paid was Rs.
# Golden Label: entailment

loan_duration_premise = 6
loan_duration_hypothesis = 5

# the hypothesis makes a statement about the duration of the loan which is also mentioned in the premise
if loan_duration_hypothesis >= loan_duration_premise:
    # check if the hypothesis estimate contradicts the duration of the loan in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise duration, we can infer entailment
    label = "entailment"

print(label)

