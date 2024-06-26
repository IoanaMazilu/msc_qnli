books_in_bin_premise = 41.0
books_removed_premise = 2.0
books_sold_premise = 33.0
books_in_bin_hypothesis = 3.0

# the hypothesis refers to the number of books in the bin, which is also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = books_in_bin_premise + books_removed_premise
# compute the number of books sold in the premise
books_sold_premise_ratio = books_sold_premise / total_books_premise
# compute the number of books in the bin according to the hypothesis
books_in_bin_hypothesis = books_in_bin_premise - books_sold_premise_ratio

if books_in_bin_hypothesis!= books_in_bin_premise:
    # check if the number of books in the bin in the hypothesis contradicts the number of books in the bin in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
