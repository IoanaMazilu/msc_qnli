# Premise: Gokul had 100 currency notes in all, some of which are of Rs 60 denomination and the remaining of Rs 50 denomination.
# Hypothesis: Gokul had more than 100 currency notes in all, some of which are of Rs 60 denomination and the remaining of Rs 50 denomination.
# Golden Label: contradiction

total_notes_premise = 100
total_notes_hypothesis = 100

# The hypothesis refers to the total number of currency notes Gokul had, which is also mentioned in the premise.
if total_notes_hypothesis > total_notes_premise:
    # Check if the total number of currency notes in the hypothesis contradicts the total number of currency notes mentioned in the premise.
    label = "contradiction"
else:
    # If the total number of currency notes in the hypothesis is not greater than the total number of currency notes in the premise, we can infer entailment.
    label = "entailment"

print(label)

