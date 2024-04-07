# Premise: for Mathura and B starts from Mathura with a speed of 40 kmph at 6 p.
# Hypothesis: for Mathura and B starts from Mathura with a speed of less than 40 kmph at 6 p.
# Golden Label: contradiction

speed_b_premise = 40
speed_b_hypothesis = 40

# the hypothesis talks about the speed of B mentioned in the premise
if speed_b_hypothesis >= speed_b_premise:
    # check if the hypothesis value contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

