aswin_age_premise = 0 # replace with Aswin's age from the premise
sachin_age_premise = 0 # replace with Sachin's age from the premise
sumesh_age_premise = 0 # replace with Sumesh's age from the premise

aswin_age_hypothesis = 25 # replace with Aswin's age from the hypothesis
sachin_age_hypothesis = 30 # replace with Sachin's age from the hypothesis
sumesh_age_hypothesis = 35 # replace with Sumesh's age from the hypothesis

# the hypothesis talks about the sum of ages of 3 people, referenced also in the premise
if aswin_age_hypothesis + sachin_age_hypothesis + sumesh_age_hypothesis <= 93:
    # check if the sum of ages in the hypothesis contradicts the sum of ages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the sum of ages
    # any sum of ages greater than 93 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
