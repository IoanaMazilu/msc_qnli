annual_borrowing_premise = 6000
annual_borrowing_hypothesis = 8000

# the hypothesis refers to the annual borrowing amount for Dana's college education mentioned in the premise
if annual_borrowing_premise >= annual_borrowing_hypothesis:
    # check if the premise borrowing amount contradicts the hypothesis estimate of less than 'annual_borrowing_hypothesis'
    label = "contradiction"
else:
    # if the premise borrowing amount does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
