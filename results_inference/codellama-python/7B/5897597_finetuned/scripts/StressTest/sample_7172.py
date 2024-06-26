problems_solved_premise_start = 70
problems_solved_premise_end = 125
problems_solved_hypothesis_start = 40
problems_solved_hypothesis_end = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_start < problems_solved_premise_start or problems_solved_hypothesis_end > problems_solved_premise_end:
    # check if the range of problems solved in the hypothesis contradicts the range of problems solved in the premise
    label = "contradiction"
elif problems_solved_hypothesis_start > problems_solved_premise_start and problems_solved_hypothesis_end == problems_solved_premise_end:
    # check if the range of problems solved in the hypothesis is a subset of the range of problems solved in the premise
    label = "entailment"
else:
    # if the hypothesis range does not contradict or is a subset of the premise range, we can infer neutrality
    label = "neutral"

print(label)
