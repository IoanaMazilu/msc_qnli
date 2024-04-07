# Premise: In 8 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In more than 5 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: entailment

years_premise = 8
years_hypothesis = 5

# both the premise and hypothesis refer to the same scenario but with different time frames
if years_premise <= years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # any number of years greater than 'years_hypothesis' and less than or equal to 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

