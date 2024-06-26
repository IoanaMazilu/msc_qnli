coloring_books_bought = 48.0
coloring_books_given_away_premise = 34.0
coloring_books_given_away_hypothesis = 3.0
total_coloring_books_hypothesis = coloring_books_bought - coloring_books_given_away_hypothesis

# the hypothesis refers to the number of coloring books left, which can be computed from the premise
# compute the number of coloring books left in the hypothesis
if coloring_books_given_away_hypothesis!= total_coloring_books_hypothesis:
    # check if the number of coloring books given away in the hypothesis contradicts the number of coloring books given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
