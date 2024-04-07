# Premise: If the number of such passengers that used Miami Airport was less than 8/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was 1/2 the number that used Kennedy Airport and 4 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: neutral

miami_to_kennedy_ratio_premise = 8/2
miami_to_kennedy_ratio_hypothesis = 1/2
miami_to_logan_ratio = 4

# the hypothesis refers to the same ratios of airport users as the premise 
if miami_to_kennedy_ratio_hypothesis != miami_to_kennedy_ratio_premise:
    # check if the ratio of Miami to Kennedy passengers in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

