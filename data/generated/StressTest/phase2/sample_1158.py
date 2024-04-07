# Premise: If the number of such passengers that used Miami Airport was 1/4 the number that used Kennedy Airport and 3 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Hypothesis: If the number of such passengers that used Miami Airport was less than 5/4 the number that used Kennedy Airport and 3 times the number that used Logan Airport, approximately how many millions of these passengers used Logan Airport that year?
# Golden Label: entailment

miami_to_kennedy_ratio_premise = 1/4
miami_to_kennedy_ratio_hypothesis = 5/4
miami_to_logan_ratio_premise = 3
miami_to_logan_ratio_hypothesis = 3

# the hypothesis refers to the ratios of the numbers of passengers that used Miami, Kennedy, and Logan airports, just like in the premise
if miami_to_kennedy_ratio_premise != miami_to_kennedy_ratio_hypothesis:
    # check if the ratio of the number of passengers that used Miami to the number that used Kennedy in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif miami_to_logan_ratio_premise != miami_to_logan_ratio_hypothesis:
    # check if the ratio of the number of passengers that used Miami to the number that used Logan in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ones in the premise, the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

