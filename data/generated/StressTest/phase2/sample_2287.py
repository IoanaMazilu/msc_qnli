# Premise: Four different children have jelly beans:Aaron has more than 6, Bianca has 7, Callie has 8, and Dante has 11.
# Hypothesis: Four different children have jelly beans:Aaron has 7, Bianca has 7, Callie has 8, and Dante has 11.
# Golden Label: neutral

aaron_jelly_premise = 6
aaron_jelly_hypothesis = 7
bianca_jelly_premise = 7
bianca_jelly_hypothesis = 7
callie_jelly_premise = 8
callie_jelly_hypothesis = 8
dante_jelly_premise = 11
dante_jelly_hypothesis = 11

# the hypothesis talks about the number of jelly beans each child has
# it references the same children and number of jelly beans as in the premise
if aaron_jelly_hypothesis <= aaron_jelly_premise:
    # check if the hypothesis value contradicts the estimate of more than 'aaron_jelly_premise'
    label = "contradiction"
elif bianca_jelly_hypothesis != bianca_jelly_premise or callie_jelly_hypothesis != callie_jelly_premise or dante_jelly_hypothesis != dante_jelly_premise:
    # check if the number of jelly beans for Bianca, Callie or Dante in the hypothesis contradicts the number reported in the premise 
    label = "contradiction"
elif aaron_jelly_hypothesis > aaron_jelly_premise:
    # the premise gives only an estimate for the number of jelly beans Aaron has
    # any number of jelly beans greater than 'aaron_jelly_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

