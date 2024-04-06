# Premise: At the beach, Miki and her sister both built sandcastles and then measured their heights and Miki's sandcastle was 0.8333333333333334 foot tall, and her sister's was 0.5 foot tall.
# Hypothesis: Total height of both sandcastles is 3.9.
# Golden Label: contradiction

miki_sandcastle_height_premise = 0.8333333333333334
sister_sandcastle_height_premise = 0.5
total_height_hypothesis = 3.9

# the hypothesis refers to the total height of the sandcastles, which are also mentioned in the premise
# compute the total height of the sandcastles in the premise
total_height_premise = miki_sandcastle_height_premise + sister_sandcastle_height_premise

if total_height_hypothesis != total_height_premise:
    # check if the total height in the hypothesis contradicts the total height from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

