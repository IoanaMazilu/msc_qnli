# Premise: Quarters (US $0.25) are stacked in less than 58 columns.
# Hypothesis: Quarters (US $0.25) are stacked in 18 columns.
# Golden Label: neutral

columns_premise = 58
columns_hypothesis = 18

# the hypothesis refers to the number of columns of quarters mentioned in the premise
if columns_hypothesis >= columns_premise:
    # check if the number of 'columns_hypothesis' contradicts the estimate of less than 'columns_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of columns
    # any number of columns less than 'columns_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

