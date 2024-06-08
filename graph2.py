# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# data={
#     'categories':['A','B', 'C', 'D', 'E'],
#     'values':[11,2,45,3,53]
# }

# # df=pd.DataFrame(data)
# # # print(df)
# # sns.barplot(x='categories', y='values', data=df)
# # plt.title("Bar chart")
# # plt.show()

# tips = sns.load_dataset("tips")
# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title('Box Plot')
# plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [85, 90, 78, 88, 92],
    'English': [78, 82, 85, 90, 88],
    'Science': [92, 88, 85, 87, 90]
}
df = pd.DataFrame(data)

# Bar plot
df_melt = df.melt(id_vars='Student', value_vars=['Math', 'English', 'Science'])
sns.barplot(x='Student', y='value', hue='variable', data=df_melt)
plt.title('Bar Plot of Students\' Scores')
plt.show()

# Box plot
sns.boxplot(data=df[['Math', 'English', 'Science']])
plt.title('Box Plot of Students\' Scores')
plt.show()

# Pair plot
sns.pairplot(df[['Math', 'English', 'Science']])
plt.title('Pair Plot of Students\' Scores')
plt.show()
