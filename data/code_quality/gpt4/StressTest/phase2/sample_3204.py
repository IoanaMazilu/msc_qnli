problems_solved_premise_start = 75
problems_solved_premise_end = 125
problems_solved_hypothesis_start = 35
problems_solved_hypothesis_end = 125

# the hypothesis refers to the range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_start > problems_solved_premise_start:
    # check if the start of range in the hypothesis contradicts the start of range in the premise
    label = "contradiction"
elif problems_solved_hypothesis_end != problems_solved_premise_end:
    # check if the end of range in the hypothesis contradicts the end of range in the premise
    label = "contradiction"
elif problems_solved_hypothesis_start < problems_solved_premise_start:
    # the premise only gives a specific range for the problems solved
    # a hypothesis start less than the premise start is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis ranges do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
