##Student Marks Performance Tracker

class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword
        for student in students:
            for subject, marks in student["marks"].items():
                if subject in subject_total:
                    subject_total[subject] += marks
                    subject_count[subject] += 1
                else:
                    subject_total[subject] = marks
                    subject_count[subject] = 1
        
        subject_average = {}
        for subject in subject_total:
            subject_average[subject] = subject_total[subject] / subject_count[subject]

        highest_subject = None
        max_average = 0

        for subject in subject_average:
            if subject_average[subject] > max_average:
                max_average = subject_average[subject]
                highest_subject = subject
        
        return subject_average, highest_subject