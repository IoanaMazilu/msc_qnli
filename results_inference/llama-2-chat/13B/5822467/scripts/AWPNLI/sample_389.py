books_premise = 35.0
books_bought_premise = 56.0
books_hypothesis = 92.0

# compute the total number of books in the premise
total_books_premise = books_premise + books_bought_premise

if books_hypothesis > total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
elif books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis does not contradict the number of books from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
