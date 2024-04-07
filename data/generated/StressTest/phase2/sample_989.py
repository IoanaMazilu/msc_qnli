# Premise: There are 300 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are more than 300 seniors at Morse High School, and 50% of them have cars.
# Golden Label: contradiction

seniors_premise = 300
seniors_hypothesis = 300
# the percentage of seniors who have cars is the same in both premise and hypothesis, so we don't need a separate variable for that

# the hypothesis refers to the number of seniors at Morse High School mentioned in the premise
if seniors_hypothesis != seniors_premise:
    # check if the number of seniors stated in the hypothesis contradicts the number of seniors given in the premise
    label = "contradiction"
else:
    # if the number of seniors in the hypothesis does not contradict the number given in the premise, we can infer entailment
    label = "entailment"

print(label)

