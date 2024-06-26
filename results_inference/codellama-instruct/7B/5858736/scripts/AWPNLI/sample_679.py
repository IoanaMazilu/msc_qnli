bought_coloring_books_premise = 48.0
given_away_coloring_books_premise = 34.0
given_away_more_coloring_books_premise = 3.0
total_coloring_books_premise = bought_coloring_books_premise - given_away_coloring_books_premise - given_away_more_coloring_books_premise

hypothesis_coloring_books = 12.0

if total_coloring_books_premise!= hypothesis_coloring_books:
    label = "contradiction"
else:
    label = "entailment"

print(label)
