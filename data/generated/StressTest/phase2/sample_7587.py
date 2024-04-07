# Premise: Calculate the average mark scored by Adam if he had the following scores in an examination:86, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Hypothesis: Calculate the average mark scored by Adam if he had the following scores in an examination:more than 46, 75, 72, 63 and 65 marks (out of 100) in French Language, Geography, Art and design, History and Physical Education respectively?
# Golden Label: entailment

french_language_premise = 86
geography_premise = 75
art_and_design_premise = 72
history_premise = 63
physical_education_premise = 65

french_language_hypothesis = 46
geography_hypothesis = 75
art_and_design_hypothesis = 72
history_hypothesis = 63
physical_education_hypothesis = 65

# calculating the average marks scored by Adam in the premise and the hypothesis
average_premise = (french_language_premise + geography_premise + art_and_design_premise + history_premise + physical_education_premise) / 5
average_hypothesis = (french_language_hypothesis + geography_hypothesis + art_and_design_hypothesis + history_hypothesis + physical_education_hypothesis) / 5

# the hypothesis talks about the average marks scored by Adam in an examination, referenced also in the premise
if average_hypothesis > average_premise:
    # check if the average marks scored by Adam in the hypothesis contradicts the average marks scored by Adam in the premise
    label = "contradiction"
elif average_hypothesis < average_premise:
    # any average lower than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the average marks scored by Adam in the hypothesis does not contradict the average marks scored by Adam in the premise, we can infer entailment
    label = "entailment"

print(label)

