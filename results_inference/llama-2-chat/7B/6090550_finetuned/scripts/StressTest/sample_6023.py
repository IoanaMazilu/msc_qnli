borrowed_pounds_premise = 5000
borrowed_pounds_hypothesis = 3000

# the hypothesis refers to the amount of money Dana borrows annually for her college education, which is also mentioned in the premise
if borrowed_pounds_hypothesis!= borrowed_pounds_premise:
    # check if the amount of money borrowed in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount of money borrowed in the hypothesis matches the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
