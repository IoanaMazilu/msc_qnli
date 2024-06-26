got_books_premise = 54.0
gave_books_premise = 23.0
left_books_hypothesis = 31.0

# the hypothesis refers to the number of books left in the class, which are also mentioned in the premise
# compute the number of books left in the class from the premise
left_books_premise = got_books_premise - gave_books_premise
if left_books_hypothesis!= left_books_premise:
    # check if the number of books left in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
