# Premise: Rahim bought 65 books for Rs.
# Hypothesis: Rahim bought more than 65 books for Rs.
# Golden Label: contradiction

books_bought_premise = 65
books_bought_hypothesis = 65

# the hypothesis references the number of books that Rahim bought, which is also mentioned in the premise
if books_bought_hypothesis != books_bought_premise:
    # check if the number of books bought in the hypothesis contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of books bought
    # any statement that states Rahim bought more than 'books_bought_premise' is inconsistent with the premise and hence a contradiction
    label = "contradiction"

print(label)

