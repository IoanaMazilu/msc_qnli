# Premise: John's Bank's saving amount is decreased more than 20% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 50% due to loan payment and current balance is Rs.
# Golden Label: neutral

saving_decrease_premise = 20
saving_decrease_hypothesis = 50

# the hypothesis talks about the decrease in savings, which is also referenced in the premise
if saving_decrease_hypothesis <= saving_decrease_premise:
    # check if the decrease in savings in the hypothesis contradicts the decrease in savings mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the decrease in savings
    # any greater decrease in savings is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

