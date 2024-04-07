# Premise: David's Bank's saving amount is decreased less than 60% due to loan payment and current balance is Rs.
# Hypothesis: David's Bank's saving amount is decreased 10% due to loan payment and current balance is Rs.
# Golden Label: neutral

saving_decrease_premise = 60
saving_decrease_hypothesis = 10

# the hypothesis refers to the percentage of saving amount decrease mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the 'saving_decrease_hypothesis' contradicts the estimate of saving decrease in the premise
    label = "contradiction"
elif saving_decrease_hypothesis < saving_decrease_premise:
    # the premise gives only an estimate for the decrease of saving amount
    # any decrease percent less than 'saving_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

