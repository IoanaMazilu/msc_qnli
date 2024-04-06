# Premise: Each year, salmon travel upstream, going from the ocean to the rivers where they were born and this year, 712261.0 returned to their rivers, 259378.0 of which were female salmon.
# Hypothesis: 452883.0 male salmon made the trip.
# Golden Label: entailment

total_salmon_premise = 712261.0
female_salmon_premise = 259378.0
male_salmon_hypothesis = 452883.0

# the hypothesis refers to the number of male salmon, which is implied in the premise
# compute the number of male salmon in the premise
male_salmon_premise = total_salmon_premise - female_salmon_premise
if male_salmon_hypothesis != male_salmon_premise:
    # check if the number of male salmon in the hypothesis contradicts the number of male salmon from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment" 

print(label)
