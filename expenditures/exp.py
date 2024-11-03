#taking the  input from the user that who is using this site
# name=input("ENTER YOUR NAME:-")
# print("Welcome",name.upper())
# print("Categories")
# print("select your catergories:-\n 1.INCOME \n 2.EXPENSE \n")
# c=int(input("Enter your choice:-"))

cat_dict= {
    1: "income",
    2: "expense"
}

sub_cat_dict= {
    1: {
        1: "Awards",
        2: "Coupons",
        3: "Grants"
    },

    2:{
        1: "bills",
        2: "Clothing",
        3: "Rent"
    }
}


et= int(input(f"Enter Expense type \n 1.Income \n 2.Expense"))

if et==1:
    print(" 1.Awards \n 2.Coupons \n 3.Grants \n 4.lottery \n 5.Refunds \n 6.Rental \n 7.Salary \n 8.Sale")
    sc= int(input("Enter sub category"))

elif et==2:
    print("Expense categories")        
    print(" 1.Baby \n 2.Beauty \n 3.Bills \n 4.Car \n 5.Clothing \n 6.Education \n 7.Electronics \n 8.Entertainment \n 9.Food \n 10.Health \n 11.Home \n 12.Insurance \n 13.Shopping \n 14.Social \n 15.Sport \n 16.Tax \n 17.Telephone \n 18.Transportation \n 19.Hostel \n 20.Loan to friend")
    sc= int(input())

Ioe, sub_cate= (cat_dict[et], sub_cat_dict[et][sc])

try:
    with open('db.txt', 'a') as file:
        file.write(f"{Ioe} \t {sub_cate}\t {500}\n")
    print("File created and written to successfully.")
except Exception as e:
    print(f"An error occurred: {e}")




# if c==1:
#     print("Income categories")
#     print(" 1.Awards \n 2.Coupons \n 3.Grants \n 4.lottery \n 5.Refunds \n 6.Rental \n 7.Salary \n 8.Sale")
#     sc= int(input())

    
# elif c==2:
#     print("Expense categories")        
#     print(" 1.Baby \n 2.Beauty \n 3.Bills \n 4.Car \n 5.Clothing \n 6.Education \n 7.Electronics \n 8.Entertainment \n 9.Food \n 10.Health \n 11.Home \n 12.Insurance \n 13.Shopping \n 14.Social \n 15.Sport \n 16.Tax \n 17.Telephone \n 18.Transportation \n 19.Hostel \n 20.Loan to friend")
#     sc= int(input())


