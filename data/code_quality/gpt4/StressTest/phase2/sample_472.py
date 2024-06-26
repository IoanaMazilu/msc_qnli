problems_solved_premise_low = 40
problems_solved_premise_high = 125
problems_solved_hypothesis_low = 80
problems_solved_hypothesis_high = 125

# the hypothesis provides a range of problems solved by Andy mentioned in the premise
if problems_solved_hypothesis_low < problems_solved_premise_low or problems_solved_hypothesis_high > problems_solved_premise_high:
    # check if the range in the hypothesis contradicts the range in the premise
    label = "contradiction"
elif problems_solved_hypothesis_low > problems_solved_premise_low:
    # check if the lower limit in the hypothesis is more than the lower limit in the premise
    # it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the range in the hypothesis does not contradict the range in the premise, we can infer entailment
    label = "entailment"

print(label)
