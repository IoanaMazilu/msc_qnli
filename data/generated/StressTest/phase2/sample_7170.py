# Premise: Andy solves problems 70 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems more than 30 to 125 inclusive in a Math exercise.
# Golden Label: entailment

problems_solved_premise_start = 70
problems_solved_premise_end = 125
problems_solved_hypothesis_start = 30
problems_solved_hypothesis_end = 125

# the hypothesis refers to the number of problems solved by Andy mentioned in the premise
if problems_solved_premise_start >= problems_solved_hypothesis_start:
    # check if the hypothesis contradicts the premise by saying Andy solved problems starting from a number less than 'problems_solved_premise_start'
    label = "contradiction"
elif problems_solved_hypothesis_end != problems_solved_premise_end:
    # check if the upper bound of problems solved in the hypothesis contradicts the upper bound of problems solved reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

