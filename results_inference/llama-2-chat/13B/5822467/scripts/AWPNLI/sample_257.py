pages_premise = 147.0
pages_hypothesis = 419.0

# the hypothesis refers to the number of pages left, which is also mentioned in the premise
# compute the total number of pages in the premise
total_pages_premise = pages_premise

if pages_hypothesis > total_pages_premise:
    # check if the number of pages in the hypothesis contradicts the number of pages from the premise
    label = "contradiction"
elif pages_hypothesis < total_pages_premise:
    # check if the number of pages in the hypothesis is less than the number of pages from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
