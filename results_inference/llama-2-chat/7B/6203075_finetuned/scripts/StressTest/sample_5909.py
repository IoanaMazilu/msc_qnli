maths_premise = 76
maths_hypothesis = 76
sci_premise = 65
sci_hypothesis = 65
stu_premise = 82
stu_hypothesis = 82
eng_premise = 67
eng_hypothesis = 67
bio_premise = 75
bio_hypothesis = 75

# the hypothesis talks about the marks scored by Shekar in different subjects
if maths_hypothesis <= maths_premise:
    label = "entailment"
elif sci_hypothesis <= sci_premise or stu_hypothesis <= stu_premise or eng_hypothesis <= eng_premise or bio_hypothesis <= bio_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
