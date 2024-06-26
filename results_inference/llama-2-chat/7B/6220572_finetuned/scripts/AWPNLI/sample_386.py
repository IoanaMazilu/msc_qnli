pears_keith_premise = 47.0
pears_mike_premise = 12.0
total_pears_mike_premise = pears_keith_premise + pears_mike_premise

# check if the number of pears left by Mike in the hypothesis contradicts the number of pears left by Mike from the premise
if total_pears_mike_hypothesis!= total_pears_mike_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
