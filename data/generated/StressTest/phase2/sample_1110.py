# Premise: If Johnny takes night school and scores an 88 in the course, what will his new average be?
# Hypothesis: If Johnny takes night school and scores an more than 18 in the course, what will his new average be?
# Golden Label: entailment

score_premise = 88
score_hypothesis = 18

# the hypothesis refers to the score mentioned in the premise
if score_hypothesis >= score_premise:
    # check if the estimate of 'score_hypothesis' contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

