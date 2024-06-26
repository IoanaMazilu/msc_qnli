books_premise = 5106.0
donated_books_premise = 1986.0
books_hypothesis = 3120.0

# the hypothesis refers to the number of books, which are also mentioned in the premise
# compute the number of books left in the school libraries from the premise
books_left_premise = books_premise - donated_books_premise
if books_hypothesis!= books_left_premise:
    # check if the number of books in the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
