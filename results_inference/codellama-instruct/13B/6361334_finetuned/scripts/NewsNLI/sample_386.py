name_premise = "Craig Hicks"
age_premise = 46
crime_premise = "first-degree murder"

name_hypothesis = "Craig Hicks"
crime_hypothesis = "first-degree murder"

# the hypothesis mentions the name and crime of the person indicted, which are also mentioned in the premise
# however, the hypothesis does not mention the age of the person, which cannot be entailed from the premise
label = "neutral"

print(label)
