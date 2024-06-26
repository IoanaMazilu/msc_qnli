borrow_rate_premise = 6
borrow_rate_hypothesis = 8

# the hypothesis refers to the borrowing rate mentioned in the premise
if borrow_rate_hypothesis!= borrow_rate_premise:
    # check if the borrowing rate in the hypothesis contradicts the borrowing rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
