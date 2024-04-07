# Premise: Jimmy's paper has 12, 24, 36, 48, and a blank space. What number should Jimmy B put in the blank space?
# Hypothesis: Jimmy's paper has less than 52, 24, 36, 48, and a blank space. What number should Jimmy B put in the blank space?
# Golden Label: entailment

paper_numbers_premise = [12, 24, 36, 48]
paper_numbers_hypothesis = [52, 24, 36, 48]

# the hypothesis refers to the numbers on Jimmy's paper mentioned in the premise
if any(a >= b for a, b in zip(paper_numbers_hypothesis, paper_numbers_premise)):
    # check if any number in the hypothesis contradicts the corresponding number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

