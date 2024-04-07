# Premise: Rajesh solved 80 per cent of the questions in an examination correctly.
# Hypothesis: Rajesh solved 70 per cent of the questions in an examination correctly.
# Golden Label: contradiction

questions_solved_correctly_premise = 80
questions_solved_correctly_hypothesis = 70

# the hypothesis refers to the percentage of questions Rajesh solved correctly in an examination, which is also mentioned in the premise
if questions_solved_correctly_hypothesis > questions_solved_correctly_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif questions_solved_correctly_hypothesis < questions_solved_correctly_premise:
    # check if the percentage in the hypothesis is less than the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

