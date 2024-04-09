books_premise = 35.0
books_hypothesis = 92.0

# compute the total number of books in the premise
total_books_premise = books_premise + books_hypothesis

# check if the number of books in the hypothesis contradicts the number of books from the premise
if total_books_hypothesis!= total_books_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
