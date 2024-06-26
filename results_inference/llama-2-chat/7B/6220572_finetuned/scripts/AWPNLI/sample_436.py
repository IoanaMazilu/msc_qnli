books_oak_premise = 5106.0
books_donated_premise = 1986.0
books_left_hypothesis = 3120.0

# the hypothesis refers to the number of books left in the school libraries, which is also mentioned in the premise
# compute the number of books left in the school libraries from the premise
books_left_premise = books_oak_premise - books_donated_premise
if books_left_hypothesis!= books_left_premise:
    # check if the number of books left in the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
