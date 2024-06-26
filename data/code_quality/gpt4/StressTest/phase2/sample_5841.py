problems_solved_start_premise = 74
problems_solved_start_hypothesis = 64
problems_solved_end_premise = 135
problems_solved_end_hypothesis = 135

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_start_hypothesis <= problems_solved_start_premise and problems_solved_end_hypothesis == problems_solved_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems solved in the premise
    label = "entailment"
elif problems_solved_start_hypothesis > problems_solved_start_premise or problems_solved_end_hypothesis != problems_solved_end_premise:
    # check if the range of problems in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
