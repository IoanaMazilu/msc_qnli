books_in_library_premise = 14240.0
books_per_shelf_premise = 8.0
shelves_in_library_hypothesis = 1780.0

# the hypothesis refers to the number of shelves in the library, which can be estimated from the premise
# compute the total number of shelves in the premise
total_shelves_premise = books_in_library_premise / books_per_shelf_premise
if shelves_in_library_hypothesis != total_shelves_premise:
    # check if the number of shelves in the hypothesis contradicts the number of shelves from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
