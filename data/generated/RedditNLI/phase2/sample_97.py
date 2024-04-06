# Premise: U.S. to Impose Tariffs on Another $16 Billion in Chinese Imports.
# Hypothesis: U.S. to Slap Tariffs on $16 Billion of Chinese Goods on Aug. 23.
# Golden Label: entailment

tariffs_premise = 16
tariffs_hypothesis = 16

# the hypothesis and premise mention the amount of tariffs to be imposed on Chinese imports
if tariffs_hypothesis != tariffs_premise:
    # check if the amount of tariffs in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

