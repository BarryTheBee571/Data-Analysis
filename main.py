#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('data/ColesSalesData.csv')

sales_data_df = pd.read_csv('data/ColesSalesData.csv')

df1 = pd.read_csv('ColesSalesData.csv')
df2 = pd.read_csv('ColesStoreData.csv')
merged_df = pd.merge(df1, df2, on='merge_key', how='left')   

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(sales_data_df)

def showCharts():
    sales_data_df.plot(
                    kind='bar',
                    x='Country',
                    y='AUD',
                    color='blue',
                    alpha=0.3,
                    title='Customer impact on sales')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the cost of a big mac in AUD
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()