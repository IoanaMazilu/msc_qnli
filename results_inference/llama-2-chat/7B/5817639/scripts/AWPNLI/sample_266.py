file_count_premise = float(4.0) + float(21.0)
file_count_hypothesis = float(2.0)

# compare the number of files in the hypothesis with the number of files in the premise
if file_count_hypothesis == file_count_premise:
    # if the number of files in the hypothesis is equal to the number of files in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of files in the hypothesis contradicts the number of files in the premise, we can infer contradiction
    label = "contradiction"

print(label)
