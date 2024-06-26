chairs_per_row_premise = 16.0
rows_premise = 27.0
total_chairs_premise = chairs_per_row_premise * rows_premise

hypothesis_chairs = 433.0

if hypothesis_chairs!= total_chairs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
