# define variables with representative names for the numerical entities in both inputs
andy_murray_premise = 1
djokovic_hypothesis = 5

# extract all quantities as valid numbers (integers or floats)
andy_murray_score_premise = 765
djokovic_score_hypothesis = 674

# perform calculations if necessary
total_sets_premise = 3
total_sets_hypothesis = 3

# compare the variables
if djokovic_score_hypothesis > andy_murray_score_premise:
    # the hypothesis mentions a higher score than the premise, so there is a contradiction
    label = "contradiction"
elif total_sets_hypothesis!= total_sets_premise:
    # the hypothesis mentions a different number of sets than the premise, so there is no entailment or contradiction
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
