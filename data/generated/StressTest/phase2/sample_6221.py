# Premise: An amount of money is to be divided between Priya, Mani and Rani in the ratio of 2:4:8.
# Hypothesis: An amount of money is to be divided between Priya, Mani and Rani in the ratio of less than 2:4:8.
# Golden Label: contradiction

# ratio of money between Priya, Mani and Rani in premise
priya_premise = 2
mani_premise = 4
rani_premise = 8

# ratio of money between Priya, Mani and Rani in hypothesis
priya_hypothesis = 1.9
mani_hypothesis = 3.9
rani_hypothesis = 7.9

# the hypothesis refers to the ratio of money division mentioned in the premise
if priya_hypothesis >= priya_premise or mani_hypothesis >= mani_premise or rani_hypothesis >= rani_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)

