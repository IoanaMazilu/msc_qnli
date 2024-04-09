jim_cleans_premise = "more than 1 hour"
jim_cleans_hypothesis = 6

# define variables with representative names for the numerical entities in both inputs
jim_cleans_premise_hours = int(jim_cleans_premise)
jim_cleans_hypothesis_hours = int(jim_cleans_hypothesis)

# extract all quantities as valid numbers
if jim_cleans_premise_hours > jim_cleans_hypothesis_hours:
    # the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif jim_cleans_hypothesis_hours!= jim_cleans_premise_hours:
    # the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
