# Premise: 3750 from Anwar at 6% p.
# Hypothesis: more than 3750 from Anwar at 6% p.
# Golden Label: contradiction

amount_premise = 3750
amount_hypothesis = 3750
interest_rate = 0.06  # this value is not used in the comparison, but is extracted as it is a numerical entity in both inputs

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the 'amount_hypothesis' contradicts the amount from Anwar in the premise
    label = "contradiction"
else:
    # the premise gives the exact amount from Anwar
    # any amount less than 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

