# Premise: There are 14240.0 books in a library and they are arranged on shelves that hold 8.0 books each.
# Hypothesis: 1779.0 shelves are in the library.
# Golden Label: contradiction

books_premise = 14240.0
books_per_shelf_premise = 8.0
shelves_hypothesis = 1779.0

# the hypothesis refers to the number of shelves, which is also inferred in the premise
# compute the number of shelves in the premise
shelves_premise = books_premise / books_per_shelf_premise
if shelves_hypothesis != shelves_premise:
    # check if the number of shelves in the hypothesis contradicts the number of shelves inferred from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

