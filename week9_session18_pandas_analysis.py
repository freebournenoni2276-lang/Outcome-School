import os
import pandas as pd

print(os.getcwd())

s_score = {
    "Student_ID": [101,102,103,104,105,106,107,108],
    "Name": ["Aaliyah","Brandon","Chloe","Daniel","Ethan","Fatima","Gabriel","Hannah"],
    "Math_Score": [85,72,95,60,88,91,76,83],
    "English_Score": [78,80,88,70,84,93,74,87],
    "Science_Score": [90,75,92,65,79,89,72,85]
}

class DataAnalyzer:
    
    def __init__(self, student_score):
        self.student_score = student_score
        self.df = None
        self.sort_data = None
        self.drop_dup = None
        self.m_analyze = None
        self.e_analyze = None
        self.s_analyze = None
        self.average = None
        self.top_student = None

    def load_data(self):

        # Convert dictionary to DataFrame
        self.df = pd.DataFrame(self.student_score)

        # Save to CSV
        self.df.to_csv("student_score.csv", index=False)

        # Read it back
        self.df = pd.read_csv("student_score.csv")

        print("\nLoading Data..................")

        print(self.df)

    def clean_data(self):

        if self.df is not None:

            self.sort_data = self.df.sort_values("Name",ascending=False)
            self.drop_dup = self.df.drop_duplicates()

            print("\nCleaning Data..............")

            print("\nCleaned Data (Sorted):")
            print(self.sort_data)

    def analyze_data(self):

        if self.df is not None:

            self.m_analyze = self.df[self.df["Math_Score"] >= 80]
            self.e_analyze = self.df[self.df["English_Score"] >= 80]
            self.s_analyze = self.df[self.df["Science_Score"] >= 80]
            self.df["Average_Score"] = self.df[["Math_Score","English_Score","Science_Score"]].mean(axis=1)
            self.top_student = self.df.loc[self.df["Average_Score"].idxmax()]

            print("\nAnalyzing Data............")

            print("\nTop Math Students: ")
            print(self.m_analyze)

            print("\nTop English Students: ")
            print(self.e_analyze)

            print("\nTop Science Students: ")
            print(self.s_analyze)

            print("\nAverage Scores:")
            print(self.df[["Name","Average_Score"]])

            print("\nTop Performing Student:")
            print(self.top_student)


    def group_data(self):

        if self.df is not None:

            self.average = self.df.groupby("Name")[["Math_Score","English_Score","Science_Score"]].mean()

            print("\nGrouping Data.................")
            print(self.average)


# Create object
analyzer = DataAnalyzer(s_score)

# Call function
analyzer.load_data()
analyzer.clean_data()
analyzer.analyze_data()
analyzer.group_data()



