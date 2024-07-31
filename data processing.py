import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:\\Users\\LENOVO\\Downloads\\Mall_Customers.csv"
data_frame = pd.read_csv(file_path)
print(data_frame.head(10),"\n")
print(data_frame.info(),"\n")
print(data_frame.describe(),"\n")
data_frame = data_frame.dropna()
print(data_frame.sort_values(by=['Age','Annual Income (k$)']).head(10),"\n")
data_frame['Customer Satisfaction'] = 1
def fun(value):
    if value > 70:
        return "Yes"
    else:
        return "No"
 
data_frame['Customer Satisfaction'] = data_frame['Spending Score (1-100)'].apply(fun)
print(data_frame.sort_values(by=['Age','Annual Income (k$)']).head(10),"\n")

sns.set(style="ticks",palette="deep",font_scale=1.1)

fig, ax=plt.subplots(figsize=(6,6))
plt.hist(data_frame["Customer Satisfaction"],bins=15,color="b")
plt.xlabel("Customer Satisfaction")
plt.ylabel("No. of Customers")
plt.title("Analysis of Customer Satisfaction of Mall Customers")
plt.show()

fig, ax=plt.subplots(figsize=(6,6))
plt.scatter(data_frame["Age"],data_frame["Annual Income (k$)"],s=30,c="m")
plt.show()

data_frame.sort_values(by=['Age','Annual Income (k$)'],axis=0, 
                    ascending=[True,True],  
                    inplace=True)
processed_file_path = './Processed_Mall_Customer_Satisfaction.csv'
data_frame.to_csv(processed_file_path, index=False)
print(f"Processed data saved to {processed_file_path}")
