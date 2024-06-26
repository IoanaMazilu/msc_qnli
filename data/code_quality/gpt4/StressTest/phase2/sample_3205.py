problems_solved_range_low_premise = 35
problems_solved_range_high_premise = 125
problems_solved_range_low_hypothesis = 75
problems_solved_range_high_hypothesis = 125

# the hypothesis gives a range of problems solved by Andy, also mentioned in the premise
if problems_solved_range_low_hypothesis < problems_solved_range_low_premise or problems_solved_range_high_hypothesis > problems_solved_range_high_premise:
    # if the range of problems solved in the hypothesis is not within the range in the premise, it contradicts the premise
    label = "contradiction"
elif problems_solved_range_low_hypothesis > problems_solved_range_low_premise:
    # any range of problems solved that starts with a problem number higher than 'problems_solved_range_low_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the range of problems solved in the hypothesis matches the range in the premise, we can infer entailment
    label = "entailment"

print(label)
