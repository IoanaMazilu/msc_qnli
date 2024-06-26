peanuts_collected_premise = 5.0
peanuts_given_premise = 2.0
peanuts_left_hypothesis = 1.0

# the hypothesis refers to the number of peanuts left, which is also mentioned in the premise
# compute the number of peanuts left in the premise
peanuts_left_premise = peanuts_collected_premise - peanuts_given_premise
if peanuts_left_hypothesis!= peanuts_left_premise:
    # check if the number of peanuts left in the hypothesis contradicts the number of peanuts left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
