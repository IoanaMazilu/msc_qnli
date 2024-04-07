# Premise: Jane will take only 12 days to complete the same task.
# Hypothesis: Jane will take only 52 days to complete the same task.
# Golden Label: contradiction

days_premise = 12
days_hypothesis = 52

# the hypothesis refers to the number of days Jane will take to complete a task, mentioned in the premise
if days_hypothesis == days_premise:
    # check if the number of days in the hypothesis matches the number of days reported in the premise
    label = "entailment"
elif days_hypothesis < days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis is more than the number of days reported in the premise, it is a contradiction
    label = "contradiction"

print(label)

