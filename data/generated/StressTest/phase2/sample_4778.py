# Premise: In 8 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In 2 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: contradiction

lyn_future_age_ratio_premise = 8
lyn_future_age_ratio_hypothesis = 2

# the hypothesis talks about the future age ratio between Lyn and Ele, which is also referenced in the premise
if lyn_future_age_ratio_hypothesis != lyn_future_age_ratio_premise:
    # check if the future age ratio in the hypothesis contradicts the future age ratio given in the premise
    label = "contradiction"
else:
    # if the future age ratios match, the premise fully entails the hypothesis
    label = "entailment"

print(label)

