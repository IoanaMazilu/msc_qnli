# Define variables with representative names for the numerical entities in both inputs
grade_premise = 80
percentile_premise = 120
grade_hypothesis = 80
percentile_hypothesis = 120

# Extract all quantities as valid numbers (integers or floats)
grade_premise = int(grade_premise)
percentile_premise = int(percentile_premise)
grade_hypothesis = int(grade_hypothesis)
percentile_hypothesis = int(percentile_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if grade_hypothesis <= grade_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'grade_premise'
    label = "contradiction"
elif percentile_hypothesis!= percentile_premise:
    # Check if the number of grades in the hypothesis contradicts the number of grades reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
