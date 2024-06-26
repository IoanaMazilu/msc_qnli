meatballs_premise = 25.0
meatballs_given_premise = 11.0
meatballs_hypothesis = 36.0

# the hypothesis refers to the number of meatballs, which are also mentioned in the premise
# compute the total number of meatballs in the premise
total_meatballs_premise = meatballs_premise + meatballs_given_premise
if total_meatballs_hypothesis!= total_meatballs_premise:
    # check if the number of meatballs in the hypothesis contradicts the number of meatballs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
