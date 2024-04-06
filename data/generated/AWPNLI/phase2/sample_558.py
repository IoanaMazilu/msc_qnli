# Premise: Mrs. Santiago has 58.0 red roses and Mrs. Garrett has 24.0.
# Hypothesis: The total number of roses is 82.0.
# Golden Label: entailment

red_roses_santiago_premise = 58.0
red_roses_garrett_premise = 24.0
total_roses_hypothesis = 82.0

# the hypothesis refers to the total number of roses, which are also mentioned in the premise
# compute the total number of roses in the premise
total_roses_premise = red_roses_santiago_premise + red_roses_garrett_premise
if total_roses_hypothesis != total_roses_premise:
    # check if the number of roses in the hypothesis contradicts the number of roses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

