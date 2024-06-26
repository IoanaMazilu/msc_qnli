total_weight_books_premise = 42.0
average_weight_book_premise = 3.0
number_books_hypothesis = 14.0

# the hypothesis talks about the number of books, which is also referenced in the premise
# compute the total weight of the books from the premise
total_weight_books_hypothesis = total_weight_books_premise / average_weight_book_premise
if number_books_hypothesis!= total_weight_books_hypothesis:
    # check if the number of books from the hypothesis contradicts the total weight of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
