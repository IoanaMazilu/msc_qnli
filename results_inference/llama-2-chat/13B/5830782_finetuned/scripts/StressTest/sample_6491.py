annual_borrow_premise = 6500
annual_borrow_hypothesis = 1500

# the hypothesis refers to the amount of money Dana borrows annually for her college education, as stated in the premise
if annual_borrow_hypothesis!= annual_borrow_premise:
    # check if the amount of money borrowed annually in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
