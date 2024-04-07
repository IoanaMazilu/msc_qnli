# Premise: John's Bank's saving amount is decreased 30% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased less than 80% due to loan payment and current balance is Rs.
# Golden Label: entailment

decrease_percentage_premise = 30
decrease_percentage_hypothesis = 80

# The hypothesis talks about the decrease in savings due to loan payment, referenced also in the premise
if decrease_percentage_hypothesis < decrease_percentage_premise:
    # Check if the hypothesis value contradicts the 'decrease_percentage_premise'
    label = "contradiction"
else:
    # The premise gives a specific decrease percentage
    # Any decrease percentage less than 'decrease_percentage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

