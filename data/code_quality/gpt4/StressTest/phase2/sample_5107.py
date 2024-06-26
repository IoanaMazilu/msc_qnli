loan_premise = 7750
loan_hypothesis = 3750
interest_rate_premise = 6
interest_rate_hypothesis = 6

# the hypothesis refers to the loan from Anwar and its interest rate mentioned in the premise
if loan_hypothesis >= loan_premise:
    # check if the hypothesis loan amount contradicts the premise's statement of less than 'loan_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but they cannot be fully entailed from the premise
    label = "neutral"

print(label)
