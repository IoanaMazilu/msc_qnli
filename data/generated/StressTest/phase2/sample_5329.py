# Premise: If Raj was one-third as old as Rahim more than 2 years back and Raj is 17 years old now, How old is Rahim now?
# Hypothesis: If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now?
# Golden Label: neutral

raj_age_premise = 17
raj_age_hypothesis = 17
years_back_premise = 2
years_back_hypothesis = 5

# the hypothesis talks about the age of Raj and Rahim, referenced also in the premise
if raj_age_premise != raj_age_hypothesis:
    # check if the age of Raj in the hypothesis contradicts the age of Raj reported in the premise
    label = "contradiction"
elif years_back_premise != years_back_hypothesis:
    # check if the number of years back in the hypothesis contradicts the number of years back reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

