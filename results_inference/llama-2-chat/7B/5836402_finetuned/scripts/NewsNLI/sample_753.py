# define variables for the entities in the premise
score_premise = 0
score_hypothesis = 2

# define a variable for the match result in the premise
result_premise = 0

# define a variable for the match result in the hypothesis
result_hypothesis = 1

# check if the match result in the hypothesis contradicts the match result in the premise
if result_hypothesis!= result_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
