# Premise: A box of books weighs 42.0 pounds and each book weighs 3.0 pounds.
# Hypothesis: 12.0 books are there in the box.
# Golden Label: contradiction

total_weight_premise = 42.0
weight_per_book_premise = 3.0
total_books_hypothesis = 12.0

# the hypothesis refers to the total number of books, which can be estimated from the premise using the weight of each book
# compute the total number of books in the premise
total_books_premise = total_weight_premise / weight_per_book_premise
if total_books_hypothesis != total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

