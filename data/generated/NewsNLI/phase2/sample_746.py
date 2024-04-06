# Premise: Crittenton, 22, pleaded guilty in Superior Court in the District of Columbia to a misdemeanor count of possession of an unregistered firearm.
# Hypothesis: Washington Wizards player Javaris Crittenton, 22, pleads to misdemeanor count.
# Golden Label: neutral

age_premise = 22
age_hypothesis = 22

# the hypothesis mentions the age of the person and the fact that he pleaded to a misdemeanor count, which is also mentioned in the premise
# however, the hypothesis does not specify the type of misdemeanor which cannot be entailed from the premise
label = "neutral"

print(label)

