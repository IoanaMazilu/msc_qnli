# Premise: Each year, salmon travel upstream, going from the ocean to the rivers where they were born and this year, 712261.0 male and 259378.0 female salmon returned to their rivers.
# Hypothesis: 971642.0 salmon made the trip.
# Golden Label: contradiction

male_salmon_premise = 712261.0
female_salmon_premise = 259378.0
total_salmon_hypothesis = 971642.0

# the hypothesis refers to the total number of salmon, which is the sum of male and female salmon in the premise
# compute the total number of salmon from the premise
total_salmon_premise = male_salmon_premise + female_salmon_premise
if total_salmon_hypothesis != total_salmon_premise:
    # check if the total number of salmon from the hypothesis contradicts the total number of salmon from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

