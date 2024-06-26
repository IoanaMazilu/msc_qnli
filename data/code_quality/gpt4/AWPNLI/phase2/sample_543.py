books_received_premise = 54.0
books_given_premise = 23.0
books_left_hypothesis = 34.0

# the hypothesis talks about the number of books left, which is also referenced in the premise
# compute the number of books left in the premise
books_left_premise = books_received_premise - books_given_premise
if books_left_hypothesis != books_left_premise:
    # check if the number of books left in the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
