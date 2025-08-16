#Owner code Part
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

Identity=input("Enter your Identity:Owner/Customer: ")
Name=input("Enter your Name:")
if Identity=="Owner":
    Password=input("Enter Password:")
    if Password=="123456789":
        print("Welcome Master")
        a=input("What action would you like to do Add a product-Add/View Analysis-View:")
        if a=='Add':
            n=int(input("How many items would you like to add:"))
            i=0
            while(i<n):
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
                    S5 = input("Enter Date of Expiry (DD-MM-YYYY or N/A if not applicable): ")
                    if S5.upper() != "N/A":
                        try:
                            datetime.datetime.strptime(S5, "%d-%m-%Y")
                        except ValueError:
                            print("Invalid date format. Use DD-MM-YYYY or type N/A.")
                            
                    x = len(df1)
                    df1.loc[x] = [S1, S2, S3, S4, S5]

                    df1.to_csv(csv_path, index=False)
                    df1.to_excel(excel_path, index=False)

                elif Item=="F":
                    csv_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Food Items.csv"
                    excel_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Food Items.xlsx"

                    df2=pd.read_csv(csv_path)
                    F1=int(input("Enter Serial No of product:"))
                    F2=input("Enter new item:")
                    F3=int(input("Enter quantity of product:"))
                    F4=float(input("Enter price of Food Product:"))
                    F5 = input("Enter Date of Expiry (DD-MM-YYYY or N/A if not applicable): ")
                    if F5.upper() != "N/A":
                        try:
                            datetime.datetime.strptime(F5, "%d-%m-%Y")
                        except ValueError:
                            print("Invalid date format. Use DD-MM-YYYY or type N/A.")
                            
                    x = len(df2)
                    df2.loc[x]=[F1,F2,F3,F4,F5]

                    df2.to_csv(csv_path,index=False)
                    df2.to_excel(excel_path, index=False)

                elif Item == "A":
                    csv_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Accessories.csv"
                    excel_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Accessories.xlsx"

                    df3 = pd.read_csv(csv_path)

                    A1 = int(input("Enter Serial No of product:"))
                    A2 = input("Enter new item:")
                    A3 = int(input("Enter quantity of product:"))
                    A4 = float(input("Enter price of Accessories:"))

                    x =len(df3)
                    df3.loc[x] = [A1, A2, A3, A4]

                    df3.to_csv(csv_path, index=False)
                    df3.to_excel(excel_path, index=False)
                else:
                    print("Invalid item type. Please enter S, F, or A.")
                    continue
                i+=1
        if a == 'View':
            def show_sales_graph():
                df = pd.read_csv("C:/Users/S Venkat Rahul/GitHub/Pet Store.Registry.csv")
                # Convert 'Date & Time' column to datetime
                df["Date & Time"] = pd.to_datetime(df["Date & Time"], errors="coerce")
                df = df.dropna(subset=["Date & Time", "Total Amount"])
                df = df.sort_values("Date & Time")
                df["Purchased_str"] = df["Date & Time"].dt.strftime("%d-%m-%Y")
                plt.figure(figsize=(12, 6))
                plt.plot(df["Purchased_str"], df["Total Amount"], marker='o', linestyle='-', color='blue')
                plt.title("Trend in Purchase Amounts")
                plt.xlabel("Date of Purchase (DD-MM-YYYY)")
                plt.ylabel("Amount Paid (INR)")
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            show_sales_graph()
    else:
        print("Wrong Password")

# Customer Part Code
if Identity=="Customer":
    print("Hello,", Name, "How can I help you")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_items = []
    reg_path="C:/Users/S Venkat Rahul/GitHub/Pet Store.Registry.csv"

    sanitary_bill=0
    food_bill=0
    accessories_bill=0
    Total_Bill=0

    S=input("Would you like to buy some sanitary produts for your pet(Yes/No):")
    if S=="Yes":
        csv_path="C:/Users/S Venkat Rahul/GitHub/Pet Store.Sanitary.csv"
        dfs=pd.read_csv(csv_path)
        print(dfs)
        N=int(input("How many types of items would you like to have:"))
        i=1
        while i <=N:
            Serial_No = input("Enter Serial No of product you would like to buy: ")
            num = input("Enter Quantity of product: ")
            try:
                Serial_No = int(Serial_No)
                num = int(num)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if Serial_No not in dfs["Serial No"].values:
                print("Serial No not found.")
                continue
            available_qty = dfs.loc[dfs["Serial No"] == Serial_No, "Quantity"].item()
            if num > available_qty:
                print(f"Only {available_qty} units available. Please enter a lower quantity.")
                continue
            T = dfs.loc[dfs["Serial No"] == Serial_No, "Price"].item() * num
            item_row = dfs[dfs["Serial No"] == Serial_No].iloc[0]
            sanitary_bill += T
            bill_items.append({
                "Category": "Sanitary",
                "Serial No": Serial_No,
                "Item Name": item_row["Item Name"],
                "Rate": item_row["Price"],
                "Qty": num,
                "Total": T
            })
            dfs.loc[dfs["Serial No"] == Serial_No, "Quantity"] -= num
            i += 1
        dfs.to_csv(csv_path, index=False)
            
    F = input("Would you like to buy some food products for your pet (Yes/No): ")
    if F == "Yes":
        csv_path ="C:/Users/S Venkat Rahul/GitHub/Pet Store.Food Items.csv"
        dff = pd.read_csv(csv_path)
        print(dff)
        N = int(input("How many types of items would you like to have: "))
        i = 1
        while i <= N:
            Serial_No = input("Enter Serial No of product you would like to buy: ")
            num = input("Enter Quantity of product: ")
            try:
                Serial_No = int(Serial_No)
                num = int(num)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if Serial_No not in dff["Serial No"].values:
                print("Serial No not found.")
                continue
            available_qty = dff.loc[dff["Serial No"] == Serial_No, "Quantity"].item()
            if num > available_qty:
                print(f"Only {available_qty} units available. Please enter a lower quantity.")
                continue
            T = dff.loc[dff["Serial No"] == Serial_No, "Price"].item() * num
            item_row = dff[dff["Serial No"] == Serial_No].iloc[0]
            food_bill += T
            bill_items.append({
                "Category": "Food",
                "Serial No": Serial_No,
                "Item Name": item_row["Item Name"],
                "Rate": item_row["Price"],
                "Qty": num,
                "Total": T
            })
            dff.loc[dff["Serial No"] == Serial_No, "Quantity"] -= num
            i += 1
        dff.to_csv(csv_path, index=False)

    A = input("Would you like to buy some Accessories for your pet (Yes/No): ")
    if A == "Yes":
        csv_path = "C:/Users/S Venkat Rahul/GitHub/Pet Store.Accessories.csv"
        dfa = pd.read_csv(csv_path)
        print(dfa)
        N = int(input("How many types of items would you like to have: "))
        i = 1
        while i <=N:
            Serial_No = input("Enter Serial No of product you would like to buy: ")
            num = input("Enter Quantity of product: ")
            try:
                Serial_No = int(Serial_No)
                num = int(num)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if Serial_No not in dfa["Serial No"].values:
                print("Serial No not found.")
                continue
            available_qty = dfa.loc[dfa["Serial No"] == Serial_No, "Quantity"].item()
            if num > available_qty:
                print(f"Only {available_qty} units available. Please enter a lower quantity.")
                continue
            T = dfa.loc[dfa["Serial No"] == Serial_No, "Price"].item() * num
            item_row = dfa[dfa["Serial No"] == Serial_No].iloc[0]
            accessories_bill += T
            bill_items.append({
                "Category": "Accessories",
                "Serial No": Serial_No,
                "Item Name": item_row["Item Name"],
                "Rate": item_row["Price"],
                "Qty": num,
                "Total": T
            })
            dfa.loc[dfa["Serial No"] == Serial_No, "Quantity"] -= num
            i += 1
        dfa.to_csv(csv_path, index=False)

    Total_Bill=sanitary_bill+food_bill+accessories_bill

    # Registry update
    dfr = pd.read_csv(reg_path)
    new_index = len(dfr)
    receipt_no = new_index + 1
    base_receipt_folder = "C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Reciepts"
    receipt_folder = f"C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Reciepts/{receipt_no}"
    receipt_file_path = f"{receipt_folder}/Receipt_{receipt_no}.pdf"
    os.makedirs(receipt_folder, exist_ok=True)
    feedback = input("We'd love your feedback on this experience.\nYour thoughts: ")

    # Load logo images
    logo1 = mpimg.imread('C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Images/Logo.png')
    logo2 = mpimg.imread('C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Images/Dod& Cat.png')
    logo3 = mpimg.imread('C:/Users/S Venkat Rahul/GitHub/Virtual-Pet-Store/Images/Cute cat.png')
    # Build item rows
    item_lines = ""
    for item in bill_items:
        item_lines += f"{item['Category']:<12} | {item['Serial No']:<9} | {item['Item Name']:<22} | {item['Rate']:<9.2f} | {item['Qty']:<3} | {item['Total']:<10.2f}\n"

    # Full bill text
    bill_lines = [
        "{:^80}".format("Pet Store Purchase Receipt"),
        f"Receipt No: {receipt_no}",
        f"Customer Name: {Name}",
        f"Date & Time: {date}",
        "",
        "Items Purchased:",
        "-" * 100,
        "Category     | Serial No | Item Name              | Rate (₹)  | Qty | Total (₹)",
        "-" * 100,
    ]

    # Add item rows
    bill_lines += item_lines.strip().split('\n')

    # Add footer
    bill_lines += [
        "-" * 100,
        f"Total Amount Paid: ₹ {round(Total_Bill, 2)}",
        "",
        "Thank you for visiting our store"
    ]

    # Render as image
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    # Add 3 logos
    logos = [logo1, logo2, logo3]
    thank_you_index = len(bill_lines) - 1
    thank_you_y = 0.80 - thank_you_index * 0.04
    positions = [(0.1, 0.99), (0.35, thank_you_y), (0.9, 0.99)]
    for img, pos in zip(logos, positions):
        imagebox = OffsetImage(img, zoom=0.15)  # Adjust zoom for size
        ab = AnnotationBbox(imagebox, pos, frameon=False, xycoords='axes fraction')
        ax.add_artist(ab)
    # Line-by-line rendering
    for i, line in enumerate(bill_lines):
        ax.text(0.01, 0.80 - i * 0.04, line, fontsize=12, va='top', ha='left', family='monospace')
    plt.tight_layout()
    plt.savefig(receipt_file_path, format='pdf', bbox_inches='tight')
    plt.show()
    plt.close()

    new_entry = {
    "Receipt No": receipt_no,
    "Customer Name": Name,
    "Date & Time": date,
    "Total Amount": round(Total_Bill, 2),
    "Receipt": receipt_file_path,
    "Feedback": feedback
    }

    new_row = pd.DataFrame([new_entry])
    dfr = pd.concat([dfr, new_row], ignore_index=True)
    dfr.to_csv(reg_path, index=False)
