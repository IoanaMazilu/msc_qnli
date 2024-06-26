# define variables for the scores in the premise and hypothesis
english_premise = 76
mathematics_premise = 60
chemistry_premise = 72
biology_premise = 77
french_premise = 55
physics_premise = 85

english_hypothesis = 66
mathematics_hypothesis = 60
chemistry_hypothesis = 72
biology_hypothesis = 77
french_hypothesis = 55
physics_hypothesis = 85

# calculate the average score for the premise
total_premise = english_premise + mathematics_premise + chemistry_premise + biology_premise + french_premise + physics_premise
average_premise = total_premise / 6

# calculate the average score for the hypothesis
total_hypothesis = english_hypothesis + mathematics_hypothesis + chemistry_hypothesis + biology_hypothesis + french_hypothesis + physics_hypothesis
average_hypothesis = total_hypothesis / 6

# compare the average scores
if average_premise <= average_hypothesis:
    # check if the hypothesis value contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score greater than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
