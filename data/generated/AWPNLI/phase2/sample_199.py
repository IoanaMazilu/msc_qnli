# Premise: For the fifth grade play, the chairs have been put into 27.0 rows with 16.0 chairs in each row.
# Hypothesis: 433.0 chairs have been put out for the play.
# Golden Label: contradiction

rows_premise = 27.0
chairs_per_row_premise = 16.0
total_chairs_hypothesis = 433.0

# the hypothesis refers to the total number of chairs, which are also calculated in the premise
# compute the total number of chairs in the premise
total_chairs_premise = rows_premise * chairs_per_row_premise
if total_chairs_hypothesis != total_chairs_premise:
    # check if the number of chairs in the hypothesis contradicts the number of chairs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

