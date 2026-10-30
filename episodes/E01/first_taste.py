# Study hours per week and exam scores of 8 students
hours  = [2, 4, 5, 7, 9, 10, 12, 15]
scores = [48, 58, 55, 66, 70, 74, 85, 82]

average = sum(scores) / len(scores)
print("Average score:", average)

low  = scores[:4]    # the 4 who studied least
high = scores[4:]    # the 4 who studied most
print("Less study:", sum(low) / len(low))
print("More study:", sum(high) / len(high))
