annual_borrow_premise = 5000
annual_borrow_hypothesis = 3000

# the hypothesis refers to the amount of money Dana borrows annually for her college education, mentioned in the premise
if annual_borrow_hypothesis!= annual_borrow_premise:
    # check if the amount of money borrowed annually in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)