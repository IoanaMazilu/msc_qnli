lists_premise = 10
lists_hypothesis = 6

# the hypothesis refers to the number of top-10-movies lists, which is also mentioned in the premise
if lists_hypothesis < lists_premise:
    # check if the hypothesis value contradicts the premise value of at least 'lists_premise' lists
    label = "contradiction"
else:
    # if the hypothesis value is greater or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
