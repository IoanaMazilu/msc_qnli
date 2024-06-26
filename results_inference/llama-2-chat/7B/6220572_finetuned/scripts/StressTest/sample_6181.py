average_marks_premise = [86, 85, 82, 87, 85]
average_marks_hypothesis = [86, 85, 82, 87, 85]

# the hypothesis refers to the average marks in each subject mentioned in the premise
if average_marks_hypothesis == average_marks_premise:
    # check if the hypothesis values match the premise ones exactly
    label = "entailment"
else:
    # any difference in the average marks values contradicts the premise ones
    label = "contradiction"

print(label)
