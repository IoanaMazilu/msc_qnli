pears_premise = 47.0
pears_hypothesis = 13.0

# the hypothesis refers to the number of pears left by Mike, which is also mentioned in the premise
# compute the total number of pears picked by Keith and Mike
total_pears_premise = pears_premise + pears_hypothesis

# check if the number of pears left by Mike in the hypothesis contradicts the number of pears picked by Keith and Mike in the premise
if total_pears_hypothesis!= total_pears_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
