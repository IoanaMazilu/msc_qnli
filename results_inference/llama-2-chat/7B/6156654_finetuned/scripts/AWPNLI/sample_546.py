fish_mrs_sheridan = 47.0
given_fish_mrs_sheridan = 22.0
remaining_fish_mrs_sheridan = fish_mrs_sheridan - given_fish_mrs_sheridan
fish_mrs_sheridan_hypothesis = 25.0

# the hypothesis refers to the number of fish Mrs. Sheridan has now, which is also mentioned in the premise
# compute the number of fish Mrs. Sheridan has now according to the premise
remaining_fish_mrs_sheridan_premise = fish_mrs_sheridan - given_fish_mrs_sheridan
if remaining_fish_mrs_sheridan_premise!= remaining_fish_mrs_sheridan_hypothesis:
    # check if the number of fish left in the premise contradicts the number of fish left in the hypothesis
    label = "contradiction"
else:
    # if the number of fish left in the premise and the hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
