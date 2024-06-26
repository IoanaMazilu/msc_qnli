books_bargin_premise = 41.0
books_sorted_premise = 2.0
books_sold_premise = 33.0
books_hypothesis = 3.0

# the hypothesis refers to the number of books in the bargin, which are also mentioned in the premise
# compute the number of books in the bargin after the books were sorted and sold
books_bargin_post_premise = books_bargin_premise - books_sorted_premise
if books_hypothesis!= books_bargin_post_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
