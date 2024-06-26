# Define variables for the marks obtained by David in each subject
english_mark = 86
mathematics_mark = 85
physics_mark = 82
chemistry_mark = 87
biology_mark = 85

# Calculate the average mark of David
average_mark = (english_mark + mathematics_mark + physics_mark + chemistry_mark + biology_mark) / 5

# Check if the hypothesis contradicts the premise
if average_mark < 86:
    label = "contradiction"
else:
    label = "neutral"

print(label)
