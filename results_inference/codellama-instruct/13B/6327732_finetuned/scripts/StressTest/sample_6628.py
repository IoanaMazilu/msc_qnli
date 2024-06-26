# define variables for the numerical entities in the premise
less_than_8 = 1
score_2 = 2
score_3 = 3

# define variables for the numerical entities in the hypothesis
score_1 = 1
score_2 = 2
score_3 = 3

# check if the hypothesis values contradict the premise values
if score_1 <= less_than_8 or score_2 <= score_2 or score_3 <= score_3:
    # if the hypothesis values contradict the premise values, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
