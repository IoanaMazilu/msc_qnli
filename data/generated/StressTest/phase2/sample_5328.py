# Premise: If Raj was one-third as old as Rahim 5 years back and Raj is 17 years old now, How old is Rahim now?
# Hypothesis: If Raj was one-third as old as Rahim more than 2 years back and Raj is 17 years old now, How old is Rahim now?
# Golden Label: entailment

raj_age_now = 17
raj_age_past_premise = raj_age_now - 5
rahim_age_past_premise = raj_age_past_premise * 3
rahim_age_now_premise = rahim_age_past_premise + 5

raj_age_past_hypothesis = raj_age_now - 2
rahim_age_past_hypothesis = raj_age_past_hypothesis * 3
rahim_age_now_hypothesis = rahim_age_past_hypothesis + 2

# the hypothesis refers to the age of Rahim mentioned in the premise
if rahim_age_now_premise != rahim_age_now_hypothesis:
    # check if the age of Rahim in the hypothesis contradicts the age of Rahim reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

