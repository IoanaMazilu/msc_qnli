rows_premise = 27.0
chairs_per_row_premise = 16.0
total_chairs_premise = rows_premise * chairs_per_row_premise

chairs_hypothesis = 433.0

if chairs_hypothesis!= total_chairs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
