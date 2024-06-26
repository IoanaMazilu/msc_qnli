borrowed_pounds_premise = 6500
borrowed_pounds_hypothesis = 1500

# the hypothesis refers to the amount of money Dana borrows each year as stated in the premise
if borrowed_pounds_hypothesis!= borrowed_pounds_premise:
    # check if the amount of money borrowed annually in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
