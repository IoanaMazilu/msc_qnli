# Define variables for the numerical entities in the premise
math_marks_premise = 76
sci_marks_premise = 65
ss_marks_premise = 82
eng_marks_premise = 67
bio_marks_premise = 75

# Define variables for the numerical entities in the hypothesis
math_marks_hypothesis = 76
sci_marks_hypothesis = 65
ss_marks_hypothesis = 82
eng_marks_hypothesis = 67
bio_marks_hypothesis = 75

# Check if the hypothesis values contradict the premise values
if math_marks_hypothesis <= math_marks_premise:
    label = "contradiction"
elif sci_marks_hypothesis <= sci_marks_premise:
    label = "contradiction"
elif ss_marks_hypothesis <= ss_marks_premise:
    label = "contradiction"
elif eng_marks_hypothesis <= eng_marks_premise:
    label = "contradiction"
elif bio_marks_hypothesis <= bio_marks_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
