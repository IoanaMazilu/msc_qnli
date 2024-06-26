books_in_box_hypothesis = 14.0
total_weight_premise = 42.0
weight_per_book_premise = 3.0

# the hypothesis refers to the number of books in the box, which can be computed from the premise
# compute the total number of books in the premise
books_in_box_premise = total_weight_premise / weight_per_book_premise
if books_in_box_hypothesis!= books_in_box_premise:
    # check if the number of books in the box in the hypothesis contradicts the number of books in the box from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)