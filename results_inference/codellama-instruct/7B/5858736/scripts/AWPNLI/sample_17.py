# define variables for the numerical entities in the premise
jason_pears_premise = 46.0
keith_pears_premise = 47.0
mike_pears_premise = 12.0

# define variables for the numerical entities in the hypothesis
total_pears_hypothesis = 101.0

# compute the total number of pears picked in the premise
total_pears_premise = jason_pears_premise + keith_pears_premise + mike_pears_premise

# check if the total number of pears in the hypothesis contradicts the estimate of more than 'total_pears_premise'
if total_pears_hypothesis > total_pears_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
