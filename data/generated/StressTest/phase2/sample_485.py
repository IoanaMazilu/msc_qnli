# Premise: Dana borrows 6000 pounds annually for her college education.
# Hypothesis: Dana borrows 8000 pounds annually for her college education.
# Golden Label: contradiction

annual_loan_premise = 6000
annual_loan_hypothesis = 8000

# the hypothesis talks about the annual loan for college, referenced also in the premise
if annual_loan_hypothesis != annual_loan_premise:
    # check if the annual loan in the hypothesis contradicts the annual loan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

