total_books_premise = 38.0
taken_books_premise = 10.0
remaining_books_hypothesis = 26.0

# the hypothesis refers to the number of books, which are also mentioned in the premise
# compute the number of books left on the shelf in the premise
remaining_books_premise = total_books_premise - taken_books_premise
if remaining_books_hypothesis!= remaining_books_premise:
    # check if the number of books from the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
