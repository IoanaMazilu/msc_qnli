# Premise: Andy solves problems 80 to 125 inclusive in a Math exercise.
# Hypothesis: Andy solves problems more than 40 to 125 inclusive in a Math exercise.
# Golden Label: entailment

problems_solved_min_premise = 80
problems_solved_max_premise = 125
problems_solved_min_hypothesis = 40
problems_solved_max_hypothesis = 125

# the hypothesis talks about the number of problems Andy solves in a Math exercise, mentioned also in the premise
if problems_solved_min_hypothesis > problems_solved_min_premise:
    # check if the minimum number of problems solved in the hypothesis contradicts the minimum number of problems solved in the premise
    label = "contradiction"
elif problems_solved_max_hypothesis != problems_solved_max_premise:
    # check if the maximum number of problems solved in the hypothesis contradicts the maximum number of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

