# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was 58.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was 78.
# Golden Label: contradiction

golf_score_premise = 58
golf_score_hypothesis = 78

# The hypothesis talks about Scott's golf score, which is also mentioned in the premise
if golf_score_premise != golf_score_hypothesis:
    # Check if the golf score in the hypothesis contradicts the golf score reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

