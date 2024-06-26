# Define variables with representative names for the numerical entities in both inputs
paper_premise = 900.0
used_paper_premise = 156.0
left_paper_hypothesis = 744.0

# Extract all quantities as valid numbers (integers or floats)
paper_premise = float(paper_premise)
used_paper_premise = float(used_paper_premise)
left_paper_hypothesis = float(left_paper_hypothesis)

# Compare the variables
if left_paper_hypothesis < paper_premise - used_paper_premise:
    # Check if the number of left paper in the hypothesis contradicts the estimate of more than 'used_paper_premise'
    label = "contradiction"
elif left_paper_hypothesis!= paper_premise - used_paper_premise:
    # Check if the number of left paper in the hypothesis contradicts the number of used paper in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
