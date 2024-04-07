# Premise: John's Bank's saving amount is decreased 12% due to loan payment and current balance is Rs.
# Hypothesis: John's Bank's saving amount is decreased less than 42% due to loan payment and current balance is Rs.
# Golden Label: entailment

decrease_percent_premise = 12
decrease_percent_hypothesis = 42

# the hypothesis talks about the percentage decrease in John's Bank's saving amount, which is also referenced in the premise
if decrease_percent_hypothesis < decrease_percent_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage stated in the premise
    label = "contradiction"
elif decrease_percent_hypothesis > decrease_percent_premise:
    # any decrease percent less than 'decrease_percent_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the decrease percentage in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

