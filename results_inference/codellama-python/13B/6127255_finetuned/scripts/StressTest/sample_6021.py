annual_borrow_premise = 5000
annual_borrow_hypothesis = 2000

# the hypothesis refers to the annual amount of money borrowed by Dana for her college education, which is also mentioned in the premise
if annual_borrow_hypothesis >= annual_borrow_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
