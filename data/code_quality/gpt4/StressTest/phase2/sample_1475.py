score_premise = 250
score_hypothesis = 350
failed_by_marks_premise = 22
failed_by_marks_hypothesis = 22

# The hypothesis refers to the marks scored by Raju and the marks by which he failed, both mentioned in the premise
if score_premise != score_hypothesis:
    # Check if the marks scored in the hypothesis contradicts the marks scored in the premise
    label = "contradiction"
elif failed_by_marks_premise != failed_by_marks_hypothesis:
    # Check if the marks by which Raju failed in the hypothesis contradicts the marks by which he failed in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
