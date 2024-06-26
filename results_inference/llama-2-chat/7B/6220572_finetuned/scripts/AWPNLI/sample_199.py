rows_premise = 27.0
chairs_per_row_premise = 16.0
total_chairs_hypothesis = 433.0

# the hypothesis talks about the total number of chairs, which is also referenced in the premise
# compute the total number of chairs from the premise
total_chairs_premise = rows_premise * chairs_per_row_premise
if total_chairs_hypothesis!= total_chairs_premise:
    # check if the total number of chairs from the hypothesis contradicts the total number of chairs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
