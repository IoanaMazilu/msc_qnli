# Premise: In 16 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In less than 26 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: entailment

lyn_ele_age_diff_premise = 16
lyn_ele_age_diff_hypothesis = 26

# the hypothesis refers to the age difference between Lyn and Ele in a number of years, also mentioned in the premise
if lyn_ele_age_diff_hypothesis < lyn_ele_age_diff_premise:
    # if the hypothesis suggests a number of years less than the premise, it contradicts it
    label = "contradiction"
elif lyn_ele_age_diff_hypothesis == lyn_ele_age_diff_premise:
    # if the hypothesis suggests the same number of years as the premise, it is entailed by the premise
    label = "entailment"
else:
    # if the hypothesis suggests a number of years higher than the premise, it does not contradict it but cannot be fully and explicitly entailed from it either
    label = "neutral"

print(label)

