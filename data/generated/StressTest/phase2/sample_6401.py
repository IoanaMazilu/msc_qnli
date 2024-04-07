# Premise: If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was 3/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: contradiction

miami_to_kennedy_ratio_premise = 1/2
miami_to_kennedy_ratio_hypothesis = 3/2
miami_to_logan_ratio_premise = 4
miami_to_logan_ratio_hypothesis = 4

# the hypothesis refers to the ratios of passengers that used Miami, Kennedy, and Logan airports in comparison to each other, which are also mentioned in the premise
if miami_to_kennedy_ratio_premise != miami_to_kennedy_ratio_hypothesis:
    # check if the ratio of passengers that used Miami to Kennedy in the hypothesis contradicts the same ratio mentioned in the premise
    label = "contradiction"
elif miami_to_logan_ratio_premise != miami_to_logan_ratio_hypothesis:
    # check if the ratio of passengers that used Miami to Logan in the hypothesis contradicts the same ratio mentioned in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

