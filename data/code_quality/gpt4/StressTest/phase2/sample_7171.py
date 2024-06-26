problems_solved_premise_min = 30
problems_solved_premise_max = 125
problems_solved_hypothesis_min = 70
problems_solved_hypothesis_max = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_max > problems_solved_premise_max or problems_solved_hypothesis_min < problems_solved_premise_min:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved mentioned in the premise
    label = "contradiction"
elif problems_solved_hypothesis_min > problems_solved_premise_min and problems_solved_hypothesis_max == problems_solved_premise_max:
    # if the range in the hypothesis is within the range of the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and cannot be inferred, we can infer neutrality
    label = "neutral"

print(label)
