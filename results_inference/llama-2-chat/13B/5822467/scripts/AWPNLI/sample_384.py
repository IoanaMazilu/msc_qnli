pears_premise = 46.0
pears_keith_premise = 47.0
eaten_pears_premise = 12.0

# define variables for the hypothesis
pears_hypothesis = 81.0

# compute the total number of pears in the premise
total_pears_premise = pears_premise + pears_keith_premise - eaten_pears_premise

if pears_hypothesis > total_pears_premise:
    # check if the number of pears in the hypothesis contradicts the estimate of total pears in the premise
    label = "contradiction"
elif pears_hypothesis < total_pears_premise:
    # check if the number of pears in the hypothesis is less than the estimate of total pears in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
