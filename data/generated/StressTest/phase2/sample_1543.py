# Premise: less than 5450 from Anwar at 6% p.
# Hypothesis: 3450 from Anwar at 6% p.
# Golden Label: neutral

borrow_from_Anwar_premise = 5450
borrow_from_Anwar_hypothesis = 3450

# the hypothesis refers to the amount borrowed from Anwar, which is also mentioned in the premise
if borrow_from_Anwar_hypothesis >= borrow_from_Anwar_premise:
    # check if the hypothesis value contradicts the estimate of less than 'borrow_from_Anwar_premise'
    label = "contradiction"
elif borrow_from_Anwar_hypothesis < borrow_from_Anwar_premise:
    # the premise gives only an estimate for the loan from Anwar
    # any amount smaller than 'borrow_from_Anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    label = "entailment"

print(label)

