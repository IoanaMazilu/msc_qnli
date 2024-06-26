pages_premise = 563.0
pages_hypothesis = 419.0
pages_read = 147.0

# the hypothesis refers to the number of pages left, which is also mentioned in the premise
# compute the total number of pages left in the premise
pages_left_premise = pages_premise - pages_read
if pages_hypothesis!= pages_left_premise:
    # check if the number of pages left in the hypothesis contradicts the number of pages left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
