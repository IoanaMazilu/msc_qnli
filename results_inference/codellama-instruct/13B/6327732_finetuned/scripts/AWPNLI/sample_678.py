bought_coloring_books_premise = 48.0
gave_away_coloring_books_premise = 34.0
gave_away_more_coloring_books_premise = 3.0
total_coloring_books_premise = bought_coloring_books_premise - gave_away_coloring_books_premise - gave_away_more_coloring_books_premise

hypothesis_coloring_books_left = 11.0

if total_coloring_books_premise!= hypothesis_coloring_books_left:
    label = "contradiction"
else:
    label = "entailment"

print(label)
