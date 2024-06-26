num_books_premise = 38.0
num_books_hypothesis = 52.0

# the hypothesis refers to the number of books on the shelf, which are also mentioned in the premise
# compute the total number of books on the shelf after Marta put more books on the shelf
total_books_premise = num_books_premise + num_books_hypothesis
if total_books_premise!= num_books_hypothesis:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
