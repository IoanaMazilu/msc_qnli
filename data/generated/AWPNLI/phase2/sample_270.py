# Premise: For Halloween Faye scored 47.0 pieces of candy and she ate 25.0 pieces the first night, and then her sister gave her 40.0 more pieces.
# Hypothesis: Faye has 62.0 pieces of candy now.
# Golden Label: entailment

scored_candy_premise = 47.0
ate_candy_premise = 25.0
received_candy_premise = 40.0
total_candy_hypothesis = 62.0

# the hypothesis refers to the total number of candies, which is also mentioned in the premise
# compute the total number of candies in the premise
total_candy_premise = scored_candy_premise - ate_candy_premise + received_candy_premise
if total_candy_hypothesis != total_candy_premise:
    # check if the number of candies in the hypothesis contradicts the number of candies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

