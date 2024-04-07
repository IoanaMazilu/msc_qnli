# Premise: Paul's salary was decreased by 50% and subsequently increased by 50 %.
# Hypothesis: Paul's salary was decreased by more than 30% and subsequently increased by 50 %.
# Golden Label: entailment

salary_decrease_premise = 50
salary_decrease_hypothesis = 30
salary_increase_premise = 50
salary_increase_hypothesis = 50

# the hypothesis refers to the percentage of decrease and increase in Paul's salary mentioned in the premise
if salary_decrease_premise <= salary_decrease_hypothesis:
    # check if the estimate of 'salary_decrease_hypothesis' contradicts the percentage of salary decrease in the premise
    label = "contradiction"
elif salary_increase_hypothesis != salary_increase_premise:
    # check if the percentage of salary increase in the hypothesis contradicts the percentage of salary increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

