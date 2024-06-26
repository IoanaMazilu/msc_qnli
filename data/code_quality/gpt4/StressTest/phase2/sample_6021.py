annual_borrow_premise = 5000
annual_borrow_hypothesis = 2000

# the hypothesis talks about the annual borrowed amount for Dana's college education, referenced also in the premise
if annual_borrow_hypothesis >= annual_borrow_premise:
    # check if the hypothesis value contradicts the stated 'annual_borrow_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
