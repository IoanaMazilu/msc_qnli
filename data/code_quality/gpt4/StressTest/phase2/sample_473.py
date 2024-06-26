problems_solved_start_premise = 80
problems_solved_end_premise = 125
problems_solved_start_hypothesis = 70
problems_solved_end_hypothesis = 125

# the hypothesis talks about the range of problems solved by Andy, which is also mentioned in the premise

if problems_solved_start_hypothesis < problems_solved_start_premise:
    # check if the starting problem number in the hypothesis contradicts the starting problem number in the premise
    label = "contradiction"
elif problems_solved_end_hypothesis != problems_solved_end_premise:
    # check if the ending problem number in the hypothesis contradicts the ending problem number in the premise
    label = "contradiction"
else:
    # if the hypothesized range doesn't contradict the premise range, we can infer entailment
    label = "entailment"

print(label)
