english_premise = 86
spanish_premise = 50
social_studies_premise = 60
fine_art_premise = 67
physical_education_premise = 79

english_hypothesis = 36
spanish_hypothesis = 50
social_studies_hypothesis = 60
fine_art_hypothesis = 67
physical_education_hypothesis = 79

# the hypothesis refers to the marks scored by Belinda in five different subjects, mentioned also in the premise
# first, we calculate the average marks in both premise and hypothesis
average_premise = (english_premise + spanish_premise + social_studies_premise + fine_art_premise + physical_education_premise) / 5
average_hypothesis = (english_hypothesis + spanish_hypothesis + social_studies_hypothesis + fine_art_hypothesis + physical_education_hypothesis) / 5

if average_premise != average_hypothesis:
    # check if the average mark in the hypothesis contradicts the average mark calculated from the premise
    label = "contradiction"
else:
    # if the average mark in the hypothesis does not contradict the average mark calculated from the premise, we can infer entailment
    label = "entailment"

print(label)
