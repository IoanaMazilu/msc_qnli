david_age_premise = 70
david_age_hypothesis = 40
daughter_age_premise = 12
daughter_age_hypothesis = 12

# the hypothesis talks about the ages of David and his daughter, which are also referenced in the premise
if david_age_hypothesis >= david_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'david_age_premise'
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for David's age
    # 'david_age_hypothesis' being less than 'david_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
