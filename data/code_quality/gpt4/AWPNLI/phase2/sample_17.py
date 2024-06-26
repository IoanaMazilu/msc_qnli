pears_jason_premise = 46.0
pears_keith_premise = 47.0
pears_mike_premise = 12.0
total_pears_hypothesis = 101.0

# the hypothesis refers to the total number of pears, which are also mentioned in the premise
# compute the total number of pears in the premise
total_pears_premise = pears_jason_premise + pears_keith_premise + pears_mike_premise
if total_pears_hypothesis != total_pears_premise:
    # check if the total number of pears in the hypothesis contradicts the total number of pears from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
