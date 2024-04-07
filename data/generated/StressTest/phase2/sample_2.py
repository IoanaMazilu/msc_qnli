# Premise: If Joe goes with her 6 years old twin brothers, and they each took 3 rides in total.
# Hypothesis: If Joe goes with her less than 6 years old twin brothers, and they each took 3 rides in total.
# Golden Label: contradiction

brothers_age_premise = 6
brothers_age_hypothesis = 6
rides_taken_premise = 3
rides_taken_hypothesis = 3

# the hypothesis talks about the ages of the brothers and the number of rides taken, referenced also in the premise
if brothers_age_hypothesis > brothers_age_premise:
    # check if the hypothesis value contradicts the age of the brothers in the premise
    label = "contradiction"
elif rides_taken_hypothesis != rides_taken_premise:
    # check if the number of rides taken in the hypothesis contradicts the number of rides taken reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact age of the brothers and the number of rides taken
    # the hypothesis gives a range of ages that includes the exact age from the premise and the same number of rides taken
    # we can infer entailment
    label = "entailment"

print(label)

