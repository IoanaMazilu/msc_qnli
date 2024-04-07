# Premise: Ramesh has solved 108 questions in an examination.
# Hypothesis: Ramesh has solved less than 508 questions in an examination.
# Golden Label: entailment

questions_solved_premise = 108
questions_solved_hypothesis = 508

# the hypothesis refers to the number of solved questions by Ramesh mentioned in the premise
if questions_solved_premise >= questions_solved_hypothesis:
    # check if the number of solved questions in the premise contradicts the estimate of less than 'questions_solved_hypothesis'
    label = "contradiction"
else:
    # any number of solved questions less than 'questions_solved_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

