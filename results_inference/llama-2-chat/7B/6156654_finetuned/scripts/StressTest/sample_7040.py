# Initialize variables for the average marks
average_geography = 0
average_history = 0
average_government = 0
average_art = 0
average_computerscience = 0
average_modernliterature = 0

# Calculate the average marks for each subject
for marks in [56, 60, 72, 85, 80]:
    if marks < average_geography:
        average_geography = marks
    if marks < average_history:
        average_history = marks
    if marks < average_government:
        average_government = marks
    if marks < average_art:
        average_art = marks
    if marks < average_computerscience:
        average_computerscience = marks
    if marks < average_modernliterature:
        average_modernliterature = marks

# Print the average marks for each subject
print("Average marks in Geography:", average_geography)
print("Average marks in History:", average_history)
print("Average marks in Government:", average_government)
print("Average marks in Art:", average_art)
print("Average marks in Computer Science:", average_computerscience)
print("Average marks in Modern Literature:", average_modernliterature)

# Check if the hypothesis is entailed by the premise
if average_geography >= 56 and average_history >= 60 and average_government >= 72 and average_art >= 85 and average_computerscience >= 80:
    label = "entailment"
elif average_geography < 56 or average_history < 60 or average_government < 72 or average_art < 85 or average_computerscience < 80:
    label = "contradiction"
else:
    label = "neutral"

print(f"Label: {label}")
