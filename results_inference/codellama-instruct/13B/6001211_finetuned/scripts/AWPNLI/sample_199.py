rows_premise = 27.0
chairs_per_row_premise = 16.0
total_chairs_hypothesis = 433.0

# the hypothesis refers to the total number of chairs, which can be calculated from the premise
# compute the total number of chairs in the premise
total_chairs_premise = rows_premise * chairs_per_row_premise
if total_chairs_hypothesis!= total_chairs_premise:
    # check if the total number of chairs in the hypothesis contradicts the total number of chairs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
