books_premise = 54.0
books_given_premise = 23.0
books_hypothesis = 34.0

# the hypothesis refers to the number of books left in the class, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = books_premise - books_given_premise
if books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
