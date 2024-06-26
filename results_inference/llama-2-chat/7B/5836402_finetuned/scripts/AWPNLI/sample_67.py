picked_limes_premise = [25.0, 32.0, 12.0]
total_limes_hypothesis = 61.0

# the hypothesis refers to the total number of limes picked, which is also mentioned in the premise
# compute the total number of limes picked in the premise
total_limes_premise = sum(picked_limes_premise)
if total_limes_hypothesis!= total_limes_premise:
    # check if the total number of limes from the hypothesis contradicts the total number of limes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
