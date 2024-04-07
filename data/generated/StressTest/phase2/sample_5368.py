# Premise: In Josephs convent school, more than 10% are boys at the same time 75% are girls students.
# Hypothesis: In Josephs convent school, 80% are boys at the same time 75% are girls students.
# Golden Label: neutral

boys_premise = 10
boys_hypothesis = 80
girls_premise = 75
girls_hypothesis = 75

# the hypothesis refers to the percentage of boys and girls students mentioned in the premise

if boys_hypothesis <= boys_premise and girls_hypothesis == girls_premise:
    # check if the percentage of 'boys_hypothesis' contradicts the number of boys percentage in the premise
    # and if the percentage of 'girls_hypothesis' contradicts the number of girls percentage in the premise
    label = "contradiction"
elif boys_hypothesis > boys_premise and girls_hypothesis == girls_premise:
    # check if the percentage of 'boys_hypothesis' is greater than the boys percentage in the premise
    # and if the percentage of 'girls_hypothesis' equals the number of girls percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

