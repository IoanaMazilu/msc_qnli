# Premise: In 6 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In less than 7 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: entailment

years_premise = 6
years_hypothesis = 7

# the hypothesis talks about the future age ratio between Lyn and Ele, referenced also in the premise
if years_hypothesis > years_premise:
    # check if the hypothesis value contradicts the estimate of 'years_premise'
    label = "contradiction"
else:
    # any number of years less than 'years_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

