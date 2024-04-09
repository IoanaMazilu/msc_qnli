annual_borrow_premise = 6500
annual_borrow_hypothesis = 1500

# the hypothesis talks about the amount Dana borrows annually, referenced also in the premise
if annual_borrow_hypothesis!= annual_borrow_premise:
    # check if the amount in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
