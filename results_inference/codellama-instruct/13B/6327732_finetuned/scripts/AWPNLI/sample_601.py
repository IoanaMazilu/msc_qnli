num_books_premise = 38.0
num_books_taken_premise = 10.0
num_books_hypothesis = 26.0

# the hypothesis refers to the number of books on the shelf, which are also mentioned in the premise
# compute the total number of books on the shelf after Marta takes some books off
total_books_premise = num_books_premise - num_books_taken_premise
if total_books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books on the shelf after Marta takes some books off
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
