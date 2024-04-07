# Premise: Dana borrows less than 8000 pounds annually for her college education.
# Hypothesis: Dana borrows 6000 pounds annually for her college education.
# Golden Label: neutral

annual_borrow_premise = 8000
annual_borrow_hypothesis = 6000

# the hypothesis refers to the annual amount Dana borrows for college which is also mentioned in the premise
if annual_borrow_hypothesis >= annual_borrow_premise:
    # check if the hypothesis value contradicts the estimate of less than 'annual_borrow_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the amount Dana borrows
    # any amount less than 'annual_borrow_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

