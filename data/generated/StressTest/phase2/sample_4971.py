# Premise: An amount of money is to be divided between Ram, Raja and Rahim in the ratio of 1:4:10.
# Hypothesis: An amount of money is to be divided between Ram, Raja and Rahim in the ratio of less than 5:4:10.
# Golden Label: entailment

# defining the ratios for the division of money for each person in the premise and hypothesis
ram_ratio_premise = 1
raja_ratio_premise = 4
rahim_ratio_premise = 10

ram_ratio_hypothesis = 5
raja_ratio_hypothesis = 4
rahim_ratio_hypothesis = 10

# the hypothesis talks about the ratio of division of money between Ram, Raja, and Rahim, referenced also in the premise
if ram_ratio_hypothesis != ram_ratio_premise:
    # check if the ram_ratio_hypothesis contradicts the ram_ratio_premise
    label = "contradiction"
elif raja_ratio_hypothesis != raja_ratio_premise or rahim_ratio_hypothesis != rahim_ratio_premise:
    # check if the ratio of division for Raja or Rahim in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis do not contradict the ratios in the premise, we can infer entailment
    label = "entailment"

print(label)

