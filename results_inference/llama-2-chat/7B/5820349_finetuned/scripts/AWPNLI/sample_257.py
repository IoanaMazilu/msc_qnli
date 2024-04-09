total_pages_premise = 563.0
read_pages_premise = 147.0
left_pages_hypothesis = 419.0

# the hypothesis refers to the number of pages left, which can be calculated from the premise
# compute the number of pages left in the premise
left_pages_premise = total_pages_premise - read_pages_premise
if left_pages_hypothesis!= left_pages_premise:
    # check if the number of pages left in the hypothesis contradicts the number of pages left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
