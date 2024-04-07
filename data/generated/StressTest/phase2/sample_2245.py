# Premise: Level-less than 2 college graduates account for 15% of Listco's sales staff.
# Hypothesis: Level-1 college graduates account for 15% of Listco's sales staff.
# Golden Label: neutral

level_graduate_premise = 2
level_graduate_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis refers to the level of college graduates and their percentage in Listco's sales staff mentioned in the premise
if level_graduate_hypothesis >= level_graduate_premise:
    # check if the level of college graduate in the hypothesis contradicts the level mentioned in the premise
    label = "contradiction"
elif percentage_premise != percentage_hypothesis:
    # check if the percentage of level-1 graduates in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

