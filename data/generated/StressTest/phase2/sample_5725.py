# Premise: Rajesh solved more than 20 per cent of the questions in an examination correctly.
# Hypothesis: Rajesh solved 80 per cent of the questions in an examination correctly.
# Golden Label: neutral

questions_solved_correctly_premise = 20
questions_solved_correctly_hypothesis = 80

# the hypothesis refers to the percentage of correctly solved questions by Rajesh, mentioned in the premise
if questions_solved_correctly_hypothesis <= questions_solved_correctly_premise:
    # check if the hypothesis value contradicts the estimate of more than 'questions_solved_correctly_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of correctly solved questions
    # any percentage greater than 'questions_solved_correctly_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

