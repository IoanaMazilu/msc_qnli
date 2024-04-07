# Premise: Raja's Bank's saving amount is decreased less than 70% due to loan payment and current balance is Rs.
# Hypothesis: Raja's Bank's saving amount is decreased 40% due to loan payment and current balance is Rs.
# Golden Label: neutral

decrease_percentage_premise = 70
decrease_percentage_hypothesis = 40

# the hypothesis talks about the decrease percentage of saving amount in a bank, referenced also in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'decrease_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the decrease percentage
    # any decrease percentage less than 'decrease_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

