# Premise: For the fifth grade play, the chairs have been put into 27.0 rows with 16.0 chairs in each row.
# Hypothesis: 432.0 chairs have been put out for the play.
# Golden Label: entailment

rows_premise = 27.0
chairs_per_row_premise = 16.0
total_chairs_hypothesis = 432.0

# the hypothesis refers to the total number of chairs, which is a product of the number of rows and chairs per row in the premise
# compute the total number of chairs in the premise
total_chairs_premise = rows_premise * chairs_per_row_premise
if total_chairs_hypothesis != total_chairs_premise:
    # check if the total number of chairs from the hypothesis contradicts the total number of chairs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

