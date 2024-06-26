problems_solved_premise_min = 30
problems_solved_premise_max = 125
problems_solved_hypothesis_min = 70
problems_solved_hypothesis_max = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_min < problems_solved_premise_min or problems_solved_hypothesis_max > problems_solved_premise_max:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_solved_hypothesis_min > problems_solved_premise_min and problems_solved_hypothesis_max < problems_solved_premise_max:
    # check if the range of problems solved in the hypothesis is fully included in the range of problems solved in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but also are not fully included, we can infer neutrality
    label = "neutral"

print(label)
