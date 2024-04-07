# Premise: Listco employs 90 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Listco employs more than 50 level-1 employees, 30 of whom are college graduates.
# Golden Label: entailment

level1_employees_premise = 90
level1_employees_hypothesis = 50
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis talks about the number of level-1 employees and graduates at Listco, referenced also in the premise
if level1_employees_premise <= level1_employees_hypothesis:
    # check if the estimate of 'level1_employees_hypothesis' contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

