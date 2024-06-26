# the premise and hypothesis both refer to the average marks of a student in different subjects

# calculate the average marks in each subject in the premise
geography_average = 60
history_and_government_average = 72
art_average = 85
computer_science_average = 80
modern_literature_average = 85

# calculate the average marks in each subject in the hypothesis
hypothesis_geography_average = 56
hypothesis_history_and_government_average = 72
hypothesis_art_average = 85
hypothesis_computer_science_average = 80
hypothesis_modern_literature_average = 85

# check if the average marks in each subject in the hypothesis contradict the average marks in the premise
if hypothesis_geography_average!= geography_average or \
   hypothesis_history_and_government_average!= history_and_government_average or \
   hypothesis_art_average!= art_average or \
   hypothesis_computer_science_average!= computer_science_average or \
   hypothesis_modern_literature_average!= modern_literature_average:
    label = "contradiction"
else:
    label = "neutral"

print(label)
