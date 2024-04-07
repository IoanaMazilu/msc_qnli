# Premise: John's Bank's saving amount is decreased less than 42% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased 12% due to loan payment and current balance is Rs.
# Golden Label: neutral

decrease_percentage_premise = 42
decrease_percentage_hypothesis = 12

# the hypothesis refers to the decrease percentage in John's bank saving amount due to loan payment, which is also mentioned in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the decrease percentage in the hypothesis contradicts the premise
    label = "contradiction"
elif decrease_percentage_hypothesis < decrease_percentage_premise:
    # the premise gives an estimate for the decrease percentage, any decrease percentage less than 'decrease_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

