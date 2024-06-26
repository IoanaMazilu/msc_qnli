saved_dollars_premise = 21
allowance_dollars_premise = 15
wins_premise = 6
total_dollars_hypothesis = 220.0

# the hypothesis refers to the total amount of dollars, which are also mentioned in the premise
# compute the total amount of dollars in the premise
total_dollars_premise = saved_dollars_premise + allowance_dollars_premise * wins_premise
if total_dollars_hypothesis!= total_dollars_premise:
    # check if the total amount of dollars in the hypothesis contradicts the total amount of dollars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)