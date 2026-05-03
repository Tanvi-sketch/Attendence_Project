import math

def attendance_percentage(total, attended):
    return (attended / total) * 100

def max_bunks(total, attended):
    return math.floor((attended - 0.75 * total) / 0.75)

def classes_needed(total, attended):
    return math.ceil((0.75 * total - attended) / 0.25)