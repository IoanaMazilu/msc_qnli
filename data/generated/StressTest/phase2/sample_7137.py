# Premise: David's Bank's saving amount is decreased 10% due to loan payment and current balance is Rs.
# Hypothesis: David's Bank's saving amount is decreased less than 60% due to loan payment and current balance is Rs.
# Golden Label: entailment

saving_decrease_premise = 10
saving_decrease_hypothesis = 60

# the hypothesis refers to the decrease in savings due to loan payments mentioned in the premise
if saving_decrease_hypothesis < saving_decrease_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the decrease percentage in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

