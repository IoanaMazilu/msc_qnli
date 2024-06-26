meatballs_hayley_premise = 25.0
meatballs_kirsten_gave = 11.0
total_meatballs_hypothesis = 36.0

# the hypothesis refers to the total number of meatballs, which are also mentioned in the premise
# compute the total number of meatballs in the premise
total_meatballs_premise = meatballs_hayley_premise + meatballs_kirsten_gave
if total_meatballs_hypothesis != total_meatballs_premise:
    # check if the number of meatballs in the hypothesis contradicts the number of meatballs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
