pages_to_read_premise = 563.0
pages_read_premise = 147.0
pages_left_hypothesis = 419.0

# the hypothesis refers to the number of pages left to read, which is also mentioned in the premise
# compute the number of pages left to read in the premise
pages_left_premise = pages_to_read_premise - pages_read_premise
if pages_left_hypothesis!= pages_left_premise:
    # check if the number of pages left from the hypothesis contradicts the number of pages left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
