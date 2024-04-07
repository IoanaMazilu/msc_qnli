# Premise: Louie takes out a three-month loan of $less than 6000.
# Hypothesis: Louie takes out a three-month loan of $1000.
# Golden Label: neutral

loan_amount_premise = 6000
loan_amount_hypothesis = 1000

# the hypothesis talks about the loan amount taken out by Louie, referenced in the premise
if loan_amount_hypothesis >= loan_amount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'loan_amount_premise'
    label = "contradiction"
elif loan_amount_hypothesis < loan_amount_premise:
    # the premise gives only an estimate for the loan amount
    # any loan amount less than 'loan_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

