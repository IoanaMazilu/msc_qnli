# Premise: Calculate Rebecca's average score in an exam if she obtained the following marks 70, 57, 69, 89 and 85 out of 100 in different subjects.
# Hypothesis: Calculate Rebecca's average score in an exam if she obtained the following marks more than 70, 57, 69, 89 and 85 out of 100 in different subjects.
# Golden Label: contradiction

# define the marks in the exam
marks_premise = [70, 57, 69, 89, 85]
marks_hypothesis = [70, 57, 69, 89, 85]

# calculate the average score in the premise
average_premise = sum(marks_premise) / len(marks_premise)

# the hypothesis does not provide explicit values for the marks, only that they are more than the given values
# thus, we cannot calculate an exact average for the hypothesis, but we know it must be more than the average in the premise
if all(mark <= average_premise for mark in marks_hypothesis):
    # check if all the marks in the hypothesis are less than or equal to the average mark in the premise
    # if so, it contradicts the hypothesis claim that the marks are more than the given values
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but we cannot calculate an exact average for the hypothesis
    # thus, we cannot fully and explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)

