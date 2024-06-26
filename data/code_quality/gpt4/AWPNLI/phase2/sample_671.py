books_start_premise = 41.0
books_sorted_premise = 2.0
books_sold_premise = 33.0
books_bin_hypothesis = 3.0

# Both premise and hypothesis refer to the number of books in the bin
# calculate the total number of books in the bin now as per the premise
books_bin_premise = books_start_premise - books_sorted_premise - books_sold_premise
if books_bin_hypothesis != books_bin_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
