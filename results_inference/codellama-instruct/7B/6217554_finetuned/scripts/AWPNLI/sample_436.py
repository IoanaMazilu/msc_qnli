books_premise = 5106.0
donated_books_premise = 1986.0
left_books_hypothesis = 3120.0

# the hypothesis talks about the number of books left in the school libraries, which are also referenced in the premise
# compute the total number of books left in the premise
left_books_premise = books_premise - donated_books_premise
if left_books_hypothesis!= left_books_premise:
    # check if the number of books left in the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
