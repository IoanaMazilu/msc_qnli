# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was 58.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was less than 88.
# Golden Label: entailment

golf_score_premise = 58
golf_score_hypothesis = 88

# the hypothesis refers to Scott's golf score average mentioned in the premise
if golf_score_premise > golf_score_hypothesis:
    # check if the value of 'golf_score_premise' contradicts the estimate of less than 'golf_score_hypothesis'
    label = "contradiction"
elif golf_score_premise != golf_score_hypothesis:
    # check if the golf score average in the hypothesis contradicts the golf score average reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

