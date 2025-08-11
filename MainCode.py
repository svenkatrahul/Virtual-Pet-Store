#Owner code Part
import pandas as pd
import datetime
Identity=input("Enter your Identity:Owner/Customer: ")
Name=input("Enter your Name:")
if Identity=="Owner":
    Password=input("Enter Password:")
    if Password=="123456789":
        print("Welcome Master")
        Item=input("What type of item do you like to change data of:S/F/A:")
        #S=Sanitary,F=Food,A=Accessories
        if Item == "S":
            csv_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Sanitary.csv"
            excel_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Sanitary.xlsx"

            df1 = pd.read_csv(csv_path)

            S1 = int(input("Enter Serial No of product: "))
            S2 = input("Enter new item: ")
            S3 = int(input("Enter quantity of product: "))
            S4 = float(input("Enter price of Sanitary Product: "))
            S5 = input("Enter Date of Expiry: ")

            x = df1["Item Name"].count()
            df1.loc[x] = [S1, S2, S3, S4, S5]

            df1.to_csv(csv_path, index=False)
            df1.to_excel(excel_path, index=False)

        if Item=="F":
            csv_path = "C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Pet Store.Food Items.csv"
            excel_path = "C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Pet Store.Food Items.xlsx"

            df2=pd.read_csv(csv_path)
            F1=int(input("Enter Serial No of product:"))
            F2=input("Enter new item:")
            F3=int(input("Enter quantity of product:"))
            F4=float(input("Enter price of Food Product:"))
            F5=input("Enter Date of Expiry:")
            x=df2["Item Name"].count()
            df2.loc[x]=[F1,F2,F3,F4,F5]

            df2.to_csv(csv_path,index=False)
            df2.to_excel(excel_path, index=False)

        if Item == "A":
            csv_path = "C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Pet Store.Accessories.csv"
            excel_path = "C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Pet Store.Accessories.xlsx"

            df3 = pd.read_csv(csv_path)

            A1 = int(input("Enter Serial No of product:"))
            A2 = input("Enter new item:")
            A3 = int(input("Enter quantity of product:"))
            A4 = float(input("Enter price of Accessories:"))

            x = df3["Item Name"].count()
            df3.loc[x] = [A1, A2, A3, A4]

            df3.to_csv(csv_path, index=False)
            df3.to_excel(excel_path, index=False)

    else:
        print("Wrong Password")
