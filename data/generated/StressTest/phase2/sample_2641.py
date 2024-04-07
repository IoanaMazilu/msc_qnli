# Premise: How much loss would Indu has suffered had she given it to Bindu for less than 5 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Golden Label: neutral

loan_term_premise = 5
loan_term_hypothesis = 2
interest_rate = 4  # both premise and hypothesis mention the same interest rate

# the hypothesis talks about the same scenario as the premise but changes the number of years
if loan_term_hypothesis >= loan_term_premise:
    # check if the hypothesis contradicts the premise's statement of the loan term being less than 'loan_term_premise'
    label = "contradiction"
elif loan_term_hypothesis < loan_term_premise:
    # the premise gives only an estimate for the loan term
    # any number of years less than 'loan_term_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

