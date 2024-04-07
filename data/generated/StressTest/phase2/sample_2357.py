# Premise: If the ratio of hybrid Tajima's to non hybrid Franks is 5:4 and there are 280 total automobiles owned by the dealership, how many hybrid Franks are there?
# Hypothesis: If the ratio of hybrid Tajima's to non hybrid Franks is more than 5:4 and there are 280 total automobiles owned by the dealership, how many hybrid Franks are there?
# Golden Label: contradiction

total_cars = 280
hybrid_to_nonhybrid_premise = 5/4
hybrid_to_nonhybrid_hypothesis = 5/4

# the hypothesis refers to the ratio of hybrid to non hybrid cars and the total number of cars, just like the premise

if total_cars != 280:
    # check if the total number of cars mentioned in the hypothesis contradicts the number of cars in the premise
    label = "contradiction"
elif hybrid_to_nonhybrid_hypothesis <= hybrid_to_nonhybrid_premise:
    # check if the ratio of hybrid to non hybrid cars in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
