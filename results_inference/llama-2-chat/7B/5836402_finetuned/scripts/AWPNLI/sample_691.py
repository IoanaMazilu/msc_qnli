saved_dollars_premise = 21
allowance_premise = 15
gambles_premise = 6
gambles_hypothesis = 6
total_dollars_hypothesis = 220

# the hypothesis refers to the total amount of dollars, which is also mentioned in the premise
# compute the total amount of dollars in the premise
total_dollars_premise = saved_dollars_premise + allowance_premise + (gambles_premise * gambles_premise)
if total_dollars_hypothesis!= total_dollars_premise:
    # check if the total amount of dollars in the hypothesis contradicts the total amount of dollars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
