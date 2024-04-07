# Premise: If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now?
# Hypothesis: If Raj was one-third as old as Rahim more than 5 years back and Raj is 17 years old now, How old is Rahim now?
# Golden Label: contradiction

raj_age_premise = 17
raj_age_past_premise = raj_age_premise - 5
rahim_age_past_premise = raj_age_past_premise * 3
rahim_age_present_premise = rahim_age_past_premise + 5

raj_age_hypothesis = 17
raj_age_past_hypothesis = raj_age_hypothesis - 5
rahim_age_past_hypothesis = raj_age_past_hypothesis * 3
rahim_age_present_hypothesis = rahim_age_past_hypothesis + 5

# the hypothesis addresses the past and present ages of Raj and Rahim, which are also mentioned in the premise
if raj_age_premise != raj_age_hypothesis or rahim_age_present_premise != rahim_age_present_hypothesis:
    # check if the current ages of Raj and Rahim in the hypothesis contradict the ages in the premise
    label = "contradiction"
elif raj_age_past_premise < raj_age_past_hypothesis or rahim_age_past_premise < rahim_age_past_hypothesis:
    # check if the past ages of Raj and Rahim in the hypothesis contradict the past ages mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

