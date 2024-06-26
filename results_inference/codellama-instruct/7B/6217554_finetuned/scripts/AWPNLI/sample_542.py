books_premise = 54.0
books_given_premise = 23.0
books_left_hypothesis = 31.0

# the hypothesis refers to the number of books left, which are also mentioned in the premise
if books_left_hypothesis!= (books_premise - books_given_premise):
    # check if the number of books left from the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
