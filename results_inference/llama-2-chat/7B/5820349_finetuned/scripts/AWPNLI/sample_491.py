collected_peanuts_premise = 5.0
given_peanuts_premise = 2.0
left_peanuts_hypothesis = 1.0

# the hypothesis refers to the number of peanuts Carol has left, which can be calculated from the premise
# compute the number of peanuts Carol has left in the premise
left_peanuts_premise = collected_peanuts_premise - given_peanuts_premise
if left_peanuts_hypothesis!= left_peanuts_premise:
    # check if the number of peanuts left in the hypothesis contradicts the number of peanuts left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
