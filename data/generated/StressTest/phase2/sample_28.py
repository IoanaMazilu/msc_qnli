# Premise: less than 8200 from Anwar at 6% p.
# Hypothesis: 4200 from Anwar at 6% p.
# Golden Label: neutral

loan_premise = 8200
loan_hypothesis = 4200

# the hypothesis refers to the loan amount from Anwar mentioned in the premise
if loan_hypothesis >= loan_premise:
    # check if the hypothesis value contradicts the estimate of less than 'loan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the loan amount
    # any loan amount less than 'loan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

