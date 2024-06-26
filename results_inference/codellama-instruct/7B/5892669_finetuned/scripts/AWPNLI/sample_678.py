bought_books_premise = 48.0
given_books_premise = 34.0
given_books_additional_premise = 3.0
left_books_hypothesis = 11.0

# the hypothesis refers to the number of coloring books left, which is also mentioned in the premise
# compute the total number of coloring books left in the premise
left_books_premise = bought_books_premise - given_books_premise - given_books_additional_premise
if left_books_hypothesis!= left_books_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
