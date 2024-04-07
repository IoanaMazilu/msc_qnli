# Premise: Calculate Renee's average score in an exam if she obtained the following marks 71, 57, 61, 80 and 88 out of 100 in different subjects.
# Hypothesis: Calculate Renee's average score in an exam if she obtained the following marks less than 81, 57, 61, 80 and 88 out of 100 in different subjects.
# Golden Label: entailment

marks_premise = [71, 57, 61, 80, 88]
marks_hypothesis = ["less than 81", 57, 61, 80, 88]

# calculate average score for Renee in the premise
average_score_premise = sum(marks_premise) / len(marks_premise)

# the hypothesis suggests that one of the marks is less than 81
# to get the maximum possible average score in the hypothesis, we replace 'less than 81' with 80
marks_hypothesis[0] = 80
average_score_hypothesis = sum(marks_hypothesis) / len(marks_hypothesis)

# compare the average scores
if average_score_hypothesis > average_score_premise:
    # if hypothesis suggests a higher average score than the premise, it is a contradiction
    label = "contradiction"
elif average_score_hypothesis < average_score_premise:
    # if hypothesis suggests a lower average score than the premise, it is an entailment
    label = "entailment"
else:
    # if the average scores are equal, it is a neutral
    label = "neutral"

print(label)

