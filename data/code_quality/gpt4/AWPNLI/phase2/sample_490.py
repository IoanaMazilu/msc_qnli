collected_peanuts_premise = 5.0
given_peanuts_premise = 2.0
remaining_peanuts_hypothesis = 3.0

# the hypothesis refers to the remaining peanuts after Carol gives some to her father, which are also mentioned in the premise
# compute the remaining peanuts in the premise
remaining_peanuts_premise = collected_peanuts_premise - given_peanuts_premise
if remaining_peanuts_hypothesis != remaining_peanuts_premise:
    # check if the remaining peanuts in the hypothesis contradicts the remaining peanuts from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
