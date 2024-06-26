annual_borrow_premise = 6500
annual_borrow_hypothesis = 1500

# the hypothesis refers to the annual amount of money borrowed by Dana for her college education, mentioned in the premise
if annual_borrow_hypothesis!= annual_borrow_premise:
    # check if the annual borrowed amount in the hypothesis contradicts the annual borrowed amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
