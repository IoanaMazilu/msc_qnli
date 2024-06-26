borrowed_pounds_premise = 6500
borrowed_pounds_hypothesis = 3500

# the hypothesis talks about the amount of money Dana borrows annually for her college education
if borrowed_pounds_hypothesis <= borrowed_pounds_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise value is less than or equal to the hypothesis value, so we can infer entailment
    label = "entailment"

print(label)
