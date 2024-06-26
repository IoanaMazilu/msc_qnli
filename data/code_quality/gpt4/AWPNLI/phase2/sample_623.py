pile_seeds_premise = 100.0
watermelons_premise = 4.0
seeds_per_watermelon_hypothesis = 21.0

# the hypothesis refers to the number of seeds per watermelon, which can be calculated from the premise
# compute the number of seeds per watermelon in the premise
seeds_per_watermelon_premise = pile_seeds_premise / watermelons_premise

if seeds_per_watermelon_hypothesis != seeds_per_watermelon_premise:
    # check if the number of seeds per watermelon in the hypothesis contradicts the calculated number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)