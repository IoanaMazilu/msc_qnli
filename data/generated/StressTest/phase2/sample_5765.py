# Premise: Dana borrows 7500 pounds annually for her college education.
# Hypothesis: Dana borrows more than 7500 pounds annually for her college education.
# Golden Label: contradiction

annual_borrow_premise = 7500
annual_borrow_hypothesis = 7500

# the hypothesis refers to the amount of money borrowed annually by Dana mentioned in the premise
if annual_borrow_hypothesis == annual_borrow_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact amount for the annual borrowed money
    # any amount greater than 'annual_borrow_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

