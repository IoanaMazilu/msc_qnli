total_pages_premise = 563.0
read_pages_premise = 147.0
remaining_pages_hypothesis = 416.0

# the hypothesis refers to the number of pages, which are also mentioned in the premise
# compute the remaining number of pages in the premise
remaining_pages_premise = total_pages_premise - read_pages_premise
if remaining_pages_hypothesis!= remaining_pages_premise:
    # check if the number of pages from the hypothesis contradicts the number of pages from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)