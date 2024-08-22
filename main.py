import pandas as pd
import matplotlib.pyplot as plt

quit_program = False

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

sales_df = pd.read_csv('data/ColesSalesData.csv')
store_df = pd.read_csv('data/ColesStoreData.csv')

combined_df = pd.merge(sales_df, store_df, on='Coles_StoreID')

def showSalesData():
    print(sales_df.to_string())

def showStoreData():
    print(store_df.to_string())

def showCombinedData():
    print(combined_df.to_string())

def showChartsLocation():
    combined_df.plot(kind='scatter', x='Store Location', y='Gross Sales', color='red', label='Sales')
    plt.title('Coles Sales Data by Store Location')
    plt.show()
    
def showChartsCustomers():
    combined_df.plot(kind='scatter', x='Customer Count', y='Gross Sales', color='red', label='Sales')
    plt.title('Coles Sales Data by Customer Count')
    plt.show()

def showChartsStaff():
    combined_df.plot(kind='scatter', x='Staff Count', y='Gross Sales', color='red', label='Sales')
    plt.title('Coles Sales Data by Staff Count')
    plt.show()

def userOptions():
    global quit_program
    print("""Welcome to the Coles Sales Data Visualisation Program
          
    Please select an option:
    1 - Show the Sales dataset
    2 - Show the Store dataset
    3 - Show the Combined DataFrame
    4 - Visualise Sales x Location Data
    5 - Visualise Sales x Customers Data
    6 - Visualise Sales x Staff Data
    7 - Quit Program
        """)
    
    choice = input('Enter Selection: ').strip()

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            showSalesData()
        elif choice == 2:
            showStoreData()
        elif choice == 3:
            showCombinedData()
        elif choice == 4:
            showChartsLocation()
        elif choice == 5:
            showChartsCustomers()
        elif choice == 6:
            showChartsStaff()
        elif choice == 7:
            print("Exiting program.")
            quit_program = True
        else:
            print('Please select a number between 1 and 7.')
    else:
        print('Invalid input, please enter a number.')

while not quit_program:
    userOptions()