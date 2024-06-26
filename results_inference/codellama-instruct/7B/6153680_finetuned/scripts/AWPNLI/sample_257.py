book_length = 563.0
pages_read = 147.0
remaining_pages = 419.0

# the hypothesis refers to the number of pages left for Ceasar to read
# compute the number of pages left for Ceasar to read based on the premise
remaining_pages_premise = book_length - pages_read
if remaining_pages!= remaining_pages_premise:
    # check if the number of pages left in the hypothesis contradicts the number of pages left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
