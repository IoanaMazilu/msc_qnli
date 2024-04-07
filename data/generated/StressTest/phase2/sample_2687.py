# Premise: In 16 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In more than 16 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: contradiction

years_future_premise = 16
years_future_hypothesis = 16

# the hypothesis talks about the future age relation between Lyn and Ele, referenced also in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_future_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age relation
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

