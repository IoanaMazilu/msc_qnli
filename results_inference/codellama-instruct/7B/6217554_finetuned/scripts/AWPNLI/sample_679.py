coloring_books_bought_premise = 48.0
coloring_books_given_away_premise = 34.0
coloring_books_given_away_hypothesis = 3.0
coloring_books_left_hypothesis = 12.0

# the hypothesis refers to the number of coloring books left, which are also mentioned in the premise
# compute the total number of coloring books left in the premise
coloring_books_left_premise = coloring_books_bought_premise - coloring_books_given_away_premise - coloring_books_given_away_hypothesis
if coloring_books_left_hypothesis!= coloring_books_left_premise:
    # check if the number of coloring books left in the hypothesis contradicts the number of coloring books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
