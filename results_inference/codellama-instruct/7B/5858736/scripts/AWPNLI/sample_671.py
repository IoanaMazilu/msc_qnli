books_bin_premise = 41.0
books_sold_premise = 33.0
books_sorted_premise = 2.0

# the hypothesis refers to the number of books in the bin, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = books_bin_premise - books_sorted_premise + books_sold_premise
if total_books_premise!= 3.0:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
