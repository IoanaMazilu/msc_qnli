# Premise: David Golinkin is the editor or author of eighteen books, and over 150 responsa, articles, sermons and books.
# Hypothesis: Golinkin has written eighteen books.
# Golden Label: neutral

total_books_premise = 18
total_books_hypothesis = 18

# the hypothesis talks about the number of books written by Golinkin, which is also mentioned in the premise
if total_books_hypothesis > total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

