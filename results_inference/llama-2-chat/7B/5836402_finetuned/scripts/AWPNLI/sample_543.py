received_books_premise = 54.0
given_books_premise = 23.0
remaining_books_hypothesis = 34.0

# the hypothesis refers to the number of books left in the class, which are also mentioned in the premise
# compute the number of books left in the class from the premise
remaining_books_premise = received_books_premise - given_books_premise
if remaining_books_hypothesis!= remaining_books_premise:
    # check if the number of books left in the class from the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
