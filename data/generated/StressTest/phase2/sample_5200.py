# Premise: Dana borrows more than 1000 pounds annually for her college education.
# Hypothesis: Dana borrows 4000 pounds annually for her college education.
# Golden Label: neutral

annual_loan_premise = 1000
annual_loan_hypothesis = 4000

# the hypothesis presents a specific number for Dana's annual loan, which is also mentioned in the premise
if annual_loan_hypothesis <= annual_loan_premise:
    # check if the hypothesis value contradicts the premise which mentions more than 'annual_loan_premise'
    label = "contradiction"
else:
    # the premise only states an estimate for the annual loan
    # any number greater than 'annual_loan_premise' is not in conflict with the premise, but it can't be fully entailed from it either
    label = "neutral"

print(label)

