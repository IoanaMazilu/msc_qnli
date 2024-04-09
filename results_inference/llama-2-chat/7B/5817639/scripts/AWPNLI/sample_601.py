books_premise = float(38.0)
books_hypothesis = float(26.0)

# compare the number of books in the premise and hypothesis
if books_hypothesis > books_premise:
    # check if the number of books in the hypothesis contradicts the number of books in the premise
    label = "contradiction"
elif books_hypothesis < books_premise:
    # check if the number of books in the hypothesis entails the number of books in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
