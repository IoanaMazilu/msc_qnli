# Score range for each number in the hypothesis
score_range_1 = 7
score_range_2 = 2
score_range_3 = 3
score_range_4 = 4

# Score range for each number in the premise
score_range_premise_1 = 1
score_range_premise_2 = 2
score_range_premise_3 = 3
score_range_premise_4 = 4

# Check if the score ranges in the hypothesis contradict the score ranges in the premise
if score_range_premise_1 > score_range_hypothesis_1 or score_range_premise_2 > score_range_hypothesis_2 or score_range_premise_3 > score_range_hypothesis_3 or score_range_premise_4 > score_range_hypothesis_4:
    label = "contradiction"
else:
    # Check if the scores in the hypothesis contradict the scores in the premise
    if score_range_hypothesis_1 <= score_range_premise_1 or score_range_hypothesis_2 <= score_range_premise_2 or score_range_hypothesis_3 <= score_range_premise_3 or score_range_hypothesis_4 <= score_range_premise_4:
        label = "contradiction"
    else:
        # If the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
        label = "entailment"

print(label)
