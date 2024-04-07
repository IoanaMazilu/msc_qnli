# Premise: If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 5 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was 8/2 the number that used Kennedy Airport and 5 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: contradiction

miami_to_kennedy_ratio_premise = 1/2
miami_to_kennedy_ratio_hypothesis = 8/2
miami_to_logan_ratio_premise = 5
miami_to_logan_ratio_hypothesis = 5

# the hypothesis refers to the ratios of passengers using Miami, Kennedy, and Logan airports mentioned in the premise
if miami_to_kennedy_ratio_premise != miami_to_kennedy_ratio_hypothesis:
    # check if the ratio of passengers using Miami to Kennedy in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif miami_to_logan_ratio_premise != miami_to_logan_ratio_hypothesis:
    # check if the ratio of passengers using Miami to Logan in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

