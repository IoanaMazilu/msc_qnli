# Premise: Dana borrows 7500 pounds annually for her college education.
# Hypothesis: Dana borrows more than 4500 pounds annually for her college education.
# Golden Label: entailment

annual_borrow_premise = 7500
annual_borrow_hypothesis = 4500

# the hypothesis refers to the annual amount of borrowed money by Dana for college, mentioned in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the estimate of 'annual_borrow_hypothesis' contradicts the amount of borrowed money in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

