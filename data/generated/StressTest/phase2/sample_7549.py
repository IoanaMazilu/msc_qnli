# Premise: John's Bank's saving amount is decreased less than 80% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 30% due to loan payment and current balance is Rs.
# Golden Label: neutral

saving_decrease_premise = 80
saving_decrease_hypothesis = 30

# the hypothesis refers to the decrease in savings due to loan payment mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the decrease estimate mentioned in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif saving_decrease_hypothesis < saving_decrease_premise:
    # the premise gives an estimate for the decrease in savings
    # any decrease less than 'saving_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

