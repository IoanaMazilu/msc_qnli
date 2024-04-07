# Premise: Claire has 3 books.
# Hypothesis: Claire has less than 3 books.
# Golden Label: contradiction

books_claire_premise = 3
books_claire_hypothesis = 3

# the hypothesis refers to the number of books Claire has, which is also mentioned in the premise
if books_claire_hypothesis < books_claire_premise:
    # check if the hypothesis value contradicts the exact number of 'books_claire_premise'
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

