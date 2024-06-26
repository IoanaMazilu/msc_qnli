# Defining the scores in each subject for the premise and hypothesis
english_premise = 65
physics_premise = 78
mathematics_premise = 89
chemistry_premise = 51
biology_premise = 69

english_hypothesis = 85
physics_hypothesis = 78
mathematics_hypothesis = 89
chemistry_hypothesis = 51
biology_hypothesis = 69

# Calculating the average score for the premise and hypothesis
average_premise = (english_premise + physics_premise + mathematics_premise + chemistry_premise + biology_premise) / 5
average_hypothesis = (english_hypothesis + physics_hypothesis + mathematics_hypothesis + chemistry_hypothesis + biology_hypothesis) / 5

# the hypothesis refers to the scores obtained by Nancy in different subjects mentioned in the premise
# as the English score in the hypothesis is less than the score in the premise, the hypothesis average should be less than the premise average
if english_hypothesis > english_premise:
    # check if the English score in the hypothesis contradicts the score in the premise
    label = "contradiction"
elif average_hypothesis >= average_premise:
    # Check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # the hypothesis values and averages do not contradict the premise ones, but the exact average cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
