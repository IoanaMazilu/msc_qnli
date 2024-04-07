# Premise: Level-1 college graduates account for 10% of Listco's sales staff.
# Hypothesis: Level-less than 1 college graduates account for 10% of Listco's sales staff.
# Golden Label: contradiction

level_one_graduates_premise = 10
level_less_than_one_graduates_hypothesis = 10

# the hypothesis talks about the percentage of Level-less than 1 college graduates in the sales staff, which is not mentioned in the premise
if level_less_than_one_graduates_hypothesis == level_one_graduates_premise:
    # check if the percentage of Level-less than 1 college graduates in the hypothesis contradicts the percentage of Level-1 college graduates mentioned in the premise
    label = "contradiction"
else:
    # if the percentage of Level-less than 1 college graduates in the hypothesis does not contradict the percentage of Level-1 college graduates mentioned in the premise, we infer neutrality
    label = "neutral"

print(label)

