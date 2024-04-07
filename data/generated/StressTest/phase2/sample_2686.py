# Premise: In less than 26 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In 16 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: neutral

years_premise = 26
years_hypothesis = 16

# the hypothesis refers to the same condition in the premise but with a different number of years
if years_hypothesis >= years_premise:
    # check if the hypothesis contradicts the premise by stating a number of years ahead that is greater or equal to the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the number of years ahead
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

