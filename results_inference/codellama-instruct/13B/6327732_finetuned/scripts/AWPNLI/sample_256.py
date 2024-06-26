pages_book_premise = 563.0
pages_read_premise = 147.0
pages_left_hypothesis = 416.0

# the hypothesis refers to the number of pages left to read, which are also mentioned in the premise
# compute the total number of pages read from the premise
total_pages_read_premise = pages_read_premise + pages_left_hypothesis
if total_pages_read_premise > pages_book_premise:
    # check if the number of pages read from the hypothesis contradicts the number of pages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
