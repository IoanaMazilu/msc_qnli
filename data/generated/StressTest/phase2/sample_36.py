# Premise: Louie takes out a three-month loan of $1000.
# Hypothesis: Louie takes out a three-month loan of $less than 6000.
# Golden Label: entailment

loan_premise = 1000
loan_hypothesis = 6000

# the hypothesis talks about the loan amount taken by Louie, which is also mentioned in the premise
if loan_hypothesis <= loan_premise:
    # check if the hypothesis value contradicts the loan amount in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount for the loan
    # any loan amount less than 'loan_hypothesis' and greater than 'loan_premise' is consistent with the premise and the hypothesis
    label = "neutral"

print(label)

