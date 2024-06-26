 loan_premise = 5000
loan_hypothesis = 2000

# the hypothesis refers to the amount of money Dana borrows annually for her education
if loan_hypothesis >= loan_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
