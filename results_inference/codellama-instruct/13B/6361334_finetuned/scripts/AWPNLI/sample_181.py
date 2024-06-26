num_books_premise = 38.0
num_books_added_premise = 10.0
num_books_hypothesis = 52.0

# the hypothesis refers to the total number of books on the shelf, which are also mentioned in the premise
# compute the total number of books on the shelf from the premise
total_num_books_premise = num_books_premise + num_books_added_premise
if num_books_hypothesis!= total_num_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
