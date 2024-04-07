# Premise: Dana borrows 6500 pounds annually for her college education.
# Hypothesis: Dana borrows more than 3500 pounds annually for her college education.
# Golden Label: entailment

annual_borrow_premise = 6500
annual_borrow_hypothesis = 3500

# the hypothesis refers to the amount Dana borrows annually for her education, which is also mentioned in the premise
if annual_borrow_hypothesis >= annual_borrow_premise:
    # check if the hypothesis estimate contradicts the amount borrowed by Dana in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, then it can be inferred from the premise
    label = "entailment"

print(label)

