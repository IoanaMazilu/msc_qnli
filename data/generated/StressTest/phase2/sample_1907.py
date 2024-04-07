# Premise: Lucy deposited $62500 in an investment fund that provided 12 percent annual return compounded quarterly.
# Hypothesis: Lucy deposited $more than 62500 in an investment fund that provided 12 percent annual return compounded quarterly.
# Golden Label: contradiction

deposit_premise = 62500
deposit_hypothesis = 62500
annual_return = 12

# the hypothesis refers to the amount of money deposited by Lucy, mentioned also in the premise
if deposit_hypothesis <= deposit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is greater than the premise value, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

