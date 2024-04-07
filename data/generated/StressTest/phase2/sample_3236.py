# Premise: There are 300 seniors at Morse High School, and 50% of them have cars.
# Hypothesis: There are less than 300 seniors at Morse High School, and 50% of them have cars.
# Golden Label: contradiction

seniors_premise = 300
seniors_hypothesis = 300

# the hypothesis refers to the number of seniors at Morse High School mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

