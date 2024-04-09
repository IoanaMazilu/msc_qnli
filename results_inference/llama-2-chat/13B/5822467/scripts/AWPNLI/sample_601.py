books_premise = 38.0
books_taken_premise = 10.0
books_hypothesis = 26.0

# compute the number of books left on the shelf in the premise
books_left_premise = books_premise - books_taken_premise

if books_hypothesis > books_left_premise:
    # check if the number of books left on the shelf in the hypothesis contradicts the number of books left on the shelf in the premise
    label = "contradiction"
elif books_hypothesis < books_left_premise:
    # check if the number of books left on the shelf in the hypothesis entails the number of books left on the shelf in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
