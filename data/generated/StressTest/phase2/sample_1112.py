# Premise: If Johnny takes night school and scores an 88 in the course, what will his new average be?
# Hypothesis: If Johnny takes night school and scores an 18 in the course, what will his new average be?
# Golden Label: contradiction

course_score_premise = 88
course_score_hypothesis = 18

# the hypothesis talks about the score Johnny got in his night school course
if course_score_premise != course_score_hypothesis:
    # check if the score in the hypothesis contradicts the score mentioned in the premise
    label = "contradiction"
else:
    # if the course score does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

