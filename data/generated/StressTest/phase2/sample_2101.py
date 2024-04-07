# Premise: If the number of such passengers that used Miami Airport was less than 2/2 the number that used Kennedy Airport and 5 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 5 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: neutral

miami_to_kennedy_ratio_premise = 2/2
miami_to_logan_ratio_premise = 5
miami_to_kennedy_ratio_hypothesis = 1/2
miami_to_logan_ratio_hypothesis = 5

# the hypothesis refers to the same ratios of passengers using different airports as the premise
if miami_to_kennedy_ratio_hypothesis != miami_to_kennedy_ratio_premise:
    # check if the ratio of passengers using Miami to Kennedy airports in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif miami_to_logan_ratio_hypothesis != miami_to_logan_ratio_premise:
    # check if the ratio of passengers using Miami to Logan airports in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratios stated in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

