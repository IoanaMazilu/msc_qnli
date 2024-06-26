boys_age_14_premise = 100
boys_age_15_premise = 70
boys_age_13_premise = 50
boys_age_12_premise = 60

boys_age_14_hypothesis = 80
boys_age_15_hypothesis = 70
boys_age_13_hypothesis = 50
boys_age_12_hypothesis = 60

# the hypothesis talks about the number of boys of each age in John's School, which is also mentioned in the premise
if boys_age_14_hypothesis!= boys_age_14_premise or boys_age_15_hypothesis!= boys_age_15_premise or boys_age_13_hypothesis!= boys_age_13_premise or boys_age_12_hypothesis!= boys_age_12_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
