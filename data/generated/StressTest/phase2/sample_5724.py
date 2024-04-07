# Premise: Rajesh solved 80 per cent of the questions in an examination correctly.
# Hypothesis: Rajesh solved more than 20 per cent of the questions in an examination correctly.
# Golden Label: entailment

questions_solved_premise = 80
questions_solved_hypothesis = 20

# the hypothesis refers to the percentage of correctly solved questions by Rajesh, mentioned also in the premise
if questions_solved_premise <= questions_solved_hypothesis:
    # check if the estimate of 'questions_solved_hypothesis' contradicts the percentage of correctly solved questions in the premise
    label = "contradiction"
elif questions_solved_hypothesis > questions_solved_premise:
    # check if the percentage of correctly solved questions in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

