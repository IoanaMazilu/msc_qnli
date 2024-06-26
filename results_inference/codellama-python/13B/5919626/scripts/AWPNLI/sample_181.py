# the hypothesis talks about the number of books on the shelf, which are also referenced in the premise
# find the total number of books in the premise 
total_books_premise = 38.0 + 10.0
if total_books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
