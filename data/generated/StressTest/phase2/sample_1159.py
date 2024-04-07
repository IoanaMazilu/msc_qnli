# Premise: If the number of such passengers that used Miami Airport was less than 5/4 the number that used Kennedy Airport and 3 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was 1/4 the number that used Kennedy Airport and 3 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: neutral

miami_to_kennedy_ratio_premise = 5/4
miami_to_logan_ratio_premise = 3
miami_to_kennedy_ratio_hypothesis = 1/4
miami_to_logan_ratio_hypothesis = 3

# the hypothesis refers to the ratios of passengers that used Miami Airport compared to Kennedy and Logan airports
if miami_to_kennedy_ratio_premise != miami_to_kennedy_ratio_hypothesis:
    # check if the ratio of passengers that used Miami vs Kennedy in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif miami_to_logan_ratio_premise != miami_to_logan_ratio_hypothesis:
    # check if the ratio of passengers that used Miami vs Logan in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

