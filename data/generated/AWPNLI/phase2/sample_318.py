# Premise: There are 3.0 calories in a candy bar.
# Hypothesis: 15.0 calories are there in 5.0 candy bars.
# Golden Label: entailment

calories_per_bar_premise = 3.0
calories_hypothesis = 15.0
bars_hypothesis = 5.0

# the hypothesis refers to the total calories in a number of bars, which can be inferred from the premise

# compute the total calories in the hypothesis number of bars
total_calories_premise = calories_per_bar_premise * bars_hypothesis

if calories_hypothesis != total_calories_premise:
    # check if the total calories in the hypothesis contradicts the calculated total calories in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

