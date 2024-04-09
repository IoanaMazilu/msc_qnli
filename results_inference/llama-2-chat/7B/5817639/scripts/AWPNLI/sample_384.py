pears_premise = 46.0 + 47.0 = 93.0
pears_hypothesis = 81.0

# the hypothesis refers to the total number of pears, which is also mentioned in the premise
# compute the total number of pears in the premise
total_pears_premise = pears_premise + 12.0 = 105.0

# check if the number of pears in the hypothesis contradicts the number of pears from the premise
if pears_hypothesis!= total_pears_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
