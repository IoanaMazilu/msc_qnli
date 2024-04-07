# Premise: Calculate the average mark scored by Andrea if he had the following scores in an examination:66, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
# Hypothesis: Calculate the average mark scored by Andrea if he had the following scores in an examination:less than 66, 60, 72, 77, 55 and 85 marks (out of 100) in English, Mathematics, Chemistry, Biology, French Language and Physics respectively?
# Golden Label: contradiction

english_mark_premise = 66
math_mark_premise = 60
chemistry_mark_premise = 72
biology_mark_premise = 77
french_mark_premise = 55
physics_mark_premise = 85

english_mark_hypothesis = 66
math_mark_hypothesis = 60
chemistry_mark_hypothesis = 72
biology_mark_hypothesis = 77
french_mark_hypothesis = 55
physics_mark_hypothesis = 85

# calculate the average marks for premise and hypothesis
average_mark_premise = (english_mark_premise + math_mark_premise + chemistry_mark_premise + biology_mark_premise + french_mark_premise + physics_mark_premise) / 6
average_mark_hypothesis = (english_mark_hypothesis + math_mark_hypothesis + chemistry_mark_hypothesis + biology_mark_hypothesis + french_mark_hypothesis + physics_mark_hypothesis) / 6

# the hypothesis refers to the average mark scored by Andrea mentioned in the premise
if average_mark_hypothesis >= average_mark_premise:
    # check if the 'average_mark_hypothesis' contradicts the average mark in the premise
    label = "contradiction"
else:
    # if the average mark in the hypothesis is less than the average mark in the premise, we can infer entailment
    label = "entailment"

print(label)

