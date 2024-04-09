# Define variables for the premise and hypothesis
english_premise = 66
mathematics_premise = 60
chemistry_premise = 72
biology_premise = 77
french_language_premise = 55
physics_premise = 85

# Define variables for the hypothesis
less_than_66 = 60
less_than_72 = 70
less_than_77 = 75
less_than_85 = 80

# Calculate the average mark scored by Andrea
average_mark = (english_premise + mathematics_premise + chemistry_premise + biology_premise + french_language_premise + physics_premise) / 5

# Check if the hypothesis contradicts the premise
if average_mark > less_than_66:
    label = "contradiction"
elif average_mark < less_than_72:
    label = "contradiction"
elif average_mark < less_than_77:
    label = "contradiction"
elif average_mark < less_than_85:
    label = "contradiction"
else:
    label = "entailment"

print(label)
