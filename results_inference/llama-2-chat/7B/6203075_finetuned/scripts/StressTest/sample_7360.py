boys_age_14_premise = 20
boys_age_14_hypothesis = 80
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis talks about the number of boys in each age group, which is also mentioned in the premise
if boys_age_14_hypothesis!= boys_age_14_premise:
    label = "contradiction"
elif boys_age_15_hypothesis!= boys_age_15_premise:
    label = "contradiction"
elif boys_age_13_hypothesis!= boys_age_13_premise:
    label = "contradiction"
elif boys_age_12_hypothesis!= boys_age_12_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
