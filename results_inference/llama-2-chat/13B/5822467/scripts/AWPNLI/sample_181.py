books_premise = 38.0
books_put_premise = 10.0
books_hypothesis = 52.0

# compute the total number of books on the shelf in the premise
total_books_premise = books_premise + books_put_premise

if books_hypothesis > total_books_premise:
    # check if the number of books in the hypothesis contradicts the estimate of more than 'books_put_premise'
    label = "contradiction"
elif books_hypothesis!= total_books_premise:
    # check if the number of books from the hypothesis contradicts the number of books in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
