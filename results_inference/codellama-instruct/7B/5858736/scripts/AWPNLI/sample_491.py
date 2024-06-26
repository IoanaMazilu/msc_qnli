peanuts_carol_premise = 5.0
peanuts_given_father_premise = 2.0
peanuts_carol_hypothesis = 1.0

# the hypothesis refers to the number of peanuts left, which is also mentioned in the premise
# compute the total number of peanuts collected by Carol
total_peanuts_carol_premise = peanuts_carol_premise + peanuts_given_father_premise
if total_peanuts_carol_premise!= peanuts_carol_hypothesis:
    # check if the number of peanuts left from the hypothesis contradicts the number of peanuts collected by Carol
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
