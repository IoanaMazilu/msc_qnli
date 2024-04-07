# Premise: 90 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: more than 50 students represent x percent of the boys at Jones Elementary School.
# Golden Label: entailment

boys_represented_premise = 90
boys_represented_hypothesis = 50

# the hypothesis talks about the number of boys represented in the school, as referenced in the premise
if boys_represented_hypothesis >= boys_represented_premise:
    # check if the number of boys represented in the hypothesis contradicts the number of boys represented in the premise
    label = "contradiction"
elif boys_represented_hypothesis < boys_represented_premise:
    # check if the number of boys represented in the hypothesis can be entailed from the premise
    label = "entailment"

print(label)

