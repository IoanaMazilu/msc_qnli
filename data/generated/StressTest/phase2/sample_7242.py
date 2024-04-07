# Premise: Ayisha's father's age will be twice Shankar's age after 10 years.
# Hypothesis: Ayisha's father's age will be twice Shankar's age after less than 80 years.
# Golden Label: entailment

time_premise = 10
time_hypothesis = 80

# the hypothesis refers to the time after which Ayisha's father's age is twice that of Shankar's, as stated in the premise
if time_hypothesis < time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif time_hypothesis > time_premise:
    # check if the time in the hypothesis is greater than time in the premise
    label = "entailment"
else:
    # if the time in the hypothesis is equal to time in the premise
    label = "neutral"

print(label)

