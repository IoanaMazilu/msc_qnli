male_salmon_premise = 712261.0
female_salmon_premise = 259378.0
total_salmon_hypothesis = 971639.0

# the hypothesis refers to the total number of salmon, which is also referenced in the premise
# compute the total number of salmon from the premise
total_salmon_premise = male_salmon_premise + female_salmon_premise
if total_salmon_hypothesis != total_salmon_premise:
    # check if the total number of salmon in the hypothesis contradicts the total number of salmon from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
