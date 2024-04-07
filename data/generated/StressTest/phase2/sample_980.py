# Premise: Calculate Tony'' s average score in an exam if he obtained the following marks 53, 87, 89, 80 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Tony'' s average score in an exam if he obtained the following marks more than 53, 87, 89, 80 and 78 out of 100 in different subjects.
# Golden Label: contradiction

# Scores obtained by Tony in the exam in different subjects according to the premise
marks_premise = [53, 87, 89, 80, 78]

# Calculate the average score obtained by Tony according to the premise
average_score_premise = sum(marks_premise) / len(marks_premise)

# Lower limit of scores obtained by Tony in the exam in different subjects according to the hypothesis
marks_hypothesis = [53, 87, 89, 80, 78]

# Calculate the lower limit of the average score obtained by Tony according to the hypothesis
average_score_hypothesis = sum(marks_hypothesis) / len(marks_hypothesis)

# The hypothesis refers to the average score obtained by Tony in the exam which is also mentioned in the premise
if average_score_premise < average_score_hypothesis:
    # Check if the average score in the premise is less than the lower limit of the average score in the hypothesis
    label = "contradiction"
elif average_score_premise > average_score_hypothesis:
    # Check if the average score in the premise is more than the lower limit of the average score in the hypothesis
    label = "neutral"
else:
    # If the average score in the premise is equal to the lower limit of the average score in the hypothesis, it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

