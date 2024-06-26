boys_age_14_premise = 80
boys_age_14_hypothesis = 50
boys_age_15_premise = 70
boys_age_15_hypothesis = 70
boys_age_13_premise = 50
boys_age_13_hypothesis = 50
boys_age_12_premise = 60
boys_age_12_hypothesis = 60

# the hypothesis talks about the number of boys of different ages in John's School
# we need to compare these numbers with the premise

# the hypothesis does not mention the age of boys 14, 15 and 12
# so we cannot infer entailment or contradiction based on these ages
label = "neutral"

print(label)
