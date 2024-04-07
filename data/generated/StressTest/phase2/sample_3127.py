# Premise: Ramesh has solved less than 508 questions in an examination.
# Hypothesis: Ramesh has solved 108 questions in an examination.
# Golden Label: neutral

questions_solved_premise = 508
questions_solved_hypothesis = 108

# the hypothesis talks about the number of questions solved by Ramesh in an examination, referenced also in the premise
if questions_solved_hypothesis >= questions_solved_premise:
    # check if the hypothesis value contradicts the estimate of less than 'questions_solved_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of questions solved
    # any number of questions less than 'questions_solved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

