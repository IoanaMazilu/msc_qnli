# Premise: Ramesh has solved 108 questions in an examination.
# Hypothesis: Ramesh has solved 208 questions in an examination.
# Golden Label: contradiction

questions_solved_premise = 108
questions_solved_hypothesis = 208

# the hypothesis refers to the number of questions solved by Ramesh mentioned in the premise
if questions_solved_premise != questions_solved_hypothesis:
    # check if the number of questions solved in the hypothesis contradicts the number of questions solved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

