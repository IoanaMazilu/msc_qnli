# Premise: Bhajan Singh purchased 120 reams of paper at Rs 80 per ream.
# Hypothesis: Bhajan Singh purchased 820 reams of paper at Rs 80 per ream.
# Golden Label: contradiction

paper_purchased_premise = 120
paper_purchased_hypothesis = 820
price_per_ream = 80  # This is the same in both premise and hypothesis, so no separate variables are needed

# the hypothesis refers to the number of reams of paper purchased by Bhajan Singh, mentioned also in the premise
if paper_purchased_hypothesis != paper_purchased_premise:
    # check if the number of reams purchased in the hypothesis contradicts the number of reams purchased in the premise
    label = "contradiction"
else:
    # in this case, if the hypothesis values and estimates do not contradict the premise ones, we could infer entailment
    # but this branch will not be reached, because we already know that 'paper_purchased_hypothesis' is not equal to 'paper_purchased_premise'
    label = "entailment"

print(label)

