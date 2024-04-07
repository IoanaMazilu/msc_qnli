# Premise: If the ratio of hybrid Tajima's to non hybrid Franks is more than 4:4 and there are 280 total automobiles owned by the dealership, how many hybrid Franks are there?
# Hypothesis: If the ratio of hybrid Tajima's to non hybrid Franks is 5:4 and there are 280 total automobiles owned by the dealership, how many hybrid Franks are there?
# Golden Label: neutral

ratio_premise = 4/4
ratio_hypothesis = 5/4
total_automobiles_premise = 280
total_automobiles_hypothesis = 280

# the hypothesis refers to the ratio of hybrid Tajima's to non hybrid Franks and the total number of automobiles at the dealership, both mentioned in the premise
if total_automobiles_hypothesis != total_automobiles_premise:
    # check if the total number of automobiles in the hypothesis contradicts the total number of automobiles reported in the premise
    label = "contradiction"
elif ratio_hypothesis <= ratio_premise:
    # check if the ratio of hybrid Tajima's to non hybrid Franks in the hypothesis contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of hybrid Tajima's to non hybrid Franks
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

