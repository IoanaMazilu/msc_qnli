# Premise: Tommy has 60.0 balloons and his mom gave him 34.0 balloons for his birthday.
# Hypothesis: Tommy has 94.0 balloons now.
# Golden Label: entailment

initial_balloons_premise = 60.0
received_balloons_premise = 34.0
total_balloons_hypothesis = 94.0

# the hypothesis refers to the total number of balloons, which is also referenced in the premise
# compute the total number of balloons in the premise
total_balloons_premise = initial_balloons_premise + received_balloons_premise
if total_balloons_hypothesis != total_balloons_premise:
    # check if the total number of balloons in the hypothesis contradicts the total number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

