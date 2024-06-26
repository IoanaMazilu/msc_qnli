weight_box_premise = 42.0
weight_book_premise = 3.0
weight_book_hypothesis = 14.0

# the hypothesis refers to the number of books, which are also mentioned in the premise
# compute the total weight of the books in the premise
total_weight_books_premise = weight_book_premise * weight_book_hypothesis
if total_weight_books_premise!= weight_box_premise:
    # check if the total weight of the books in the hypothesis contradicts the weight of the box from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
