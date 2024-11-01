import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE BAKERY')
mycursor.execute('USE BAKERY')
mycursor.execute('CREATE TABLE ITEMS\
                 (PRODUCT_ID varchar(5) primary key,\
                 PRODUCT_NAME varchar(25),\
                 PRODUCT_PRICE int,\
                 STOCK int)')
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('1','Red velvet cake',650,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('2','Pineapple cake',430,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('3','Light chocolate cake',430,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('4','Black forest cake',385,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('5','White forest cake',420,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('6','Blueberry cake',445,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('7','Choco chip cake',445,20)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('8','Kitkat pastry',80,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('9','Rainbow pastry',90,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('10','Nutella pastry',145,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('11','Chocolate pastry',95,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('14','Choco ball',55,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('15','Jam swiss roll',80,30)")
mycursor.execute("INSERT INTO ITEMS VALUES\
                 ('16','Choco lava cup',90,30)")

mycursor.execute('CREATE TABLE ORDERS\
                 (PRODUCT_ID varchar(5),\
                 PRODUCT_NAME varchar(25),\
                 SALES int,\
                 DATE_ORDERED date)')
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('1','Red velvet cake',10,'2022-01-05')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('3','Light chocolate cake',12,'2020-05-12')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('4','Black forest cake',5,'2019-03-23')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('5','White forest cake',2,'2018-08-14')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('6','Blueberry cake',3,'2017-04-06')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('7','Choco chip cake',12,'2016-04-17')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('8','Kitkat pastry',6,'2017-04-19')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('9','Rainbow pastry',3,'2018-07-11')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('10','Nutella pastry',14,'2017-11-26')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('11','Chocolate Morque pastry',10,'2017-12-04')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('9','Rainbow pastry',18,'2019-11-05')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('9','Rainbow pastry',12,'2022-01-13')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('13','Caramel custard slice',6,'2019-07-12')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('14','Choco ball',15,'2013-04-08')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('15','Jam swiss roll',12,'2022-01-17')")
mycursor.execute("INSERT INTO ORDERS VALUES\
                 ('16','Choco lava cup',12,'2022-01-29')")


mycursor.execute('CREATE TABLE CUSTOMERS\
                 (CUSTOMER_ID varchar(5) primary key,\
                  CUSTOMER_PHNo varchar(10) unique,\
                  CUSTOMER_NAME varchar(25),\
                  CUSTOMER_POINTS int)')
mycursor.execute("INSERT INTO CUSTOMERS VALUES\
('104','9834572289','Lucky',56)")

mycursor.execute("INSERT INTO CUSTOMERS VALUES\
('105','9733579289','Dev',220)")

mycursor.execute("INSERT INTO CUSTOMERS VALUES\
('110','7804572185','Shreya',620)")

mycursor.execute("INSERT INTO CUSTOMERS VALUES\
('113','8034570285','Subh',2020)")

mycursor.execute("INSERT INTO CUSTOMERS VALUES\
('121','8134272480','Sarthak',5401)")
mycursor.execute('create table discounts\
                 (DATE_ORDERED date,\
                 discount decimal)')
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2021-11-20',42)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2022-01-2',50)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2022-11-14',600)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2022-01-20',534)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2021-11-30',60)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2022-09-11',46)")
mycursor.execute("INSERT INTO DISCOUNTS VALUES\
('2022-09-01',320)")
mydb.commit()
print('You are ready to go!!!')
print("Please execute 'CAKE SHOP'.") 

#CAKE SHOP FILE
import random
import mysql.connector
import datetime as dt
mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin')
mycursor=mydb.cursor()
mycursor.execute('USE BAKERY')
print()
print('*'*70)
print('______________________CHERRY ON THE TOP CAKE SHOP______________________')
print('*'*70)
print()
def view():
    mycursor.execute('SELECT * FROM ITEMS ORDER BY PRODUCT_NAME')
    print('%5s'%'P_ID','%25s'%'Name','%20s'%'Price(per unit)','%10s'%'Stock')
    for i in mycursor:
        print('%5s'%i[0],'%25s'%i[1],'%20s'%i[2],'%10s'%i[3])
def view_cust():
    mycursor.execute('SELECT * FROM CUSTOMERS')
    print('%5s'%'CUSTOMER_ID','%20s'%'Ph No','%20s'%'Name','%20s'%'Points')
    for i in mycursor:
        print('%5s'%i[0],'%20s'%i[1],'%20s'%i[2],'%20s'%i[3])
def add_items():
    mycursor.execute('SELECT * FROM ITEMS')
    pid=[]
    products=[]
    for i in mycursor:
        pid.append(i[0])
        products.append(i[1].lower())
    while True:
        PRODUCT_ID=random.randint(1,100)
        PRODUCT_ID=str(PRODUCT_ID)
        if PRODUCT_ID  in pid:
            continue
        else:
            PRODUCT_NAME=input('Enter the name of the product=')
            PRODUCT_NAME=PRODUCT_NAME.lower()
            if PRODUCT_NAME in products:
                print('Item',PRODUCT_NAME,'already exists!!!!!')
            else:
                PRODUCT_PRICE=int(input('Enter the price of the product(per unit)='))
                QUANTITY_AVAILABLE=int(input('Enter the quantity(stock) of the product='))
                mycursor.execute("Insert into ITEMS values('{}','{}',{},{})".format(PRODUCT_ID,PRODUCT_NAME,PRODUCT_PRICE,QUANTITY_AVAILABLE))
                print('ITEM ADDED SUCCESSFULLY!!!!')
                view()
                mydb.commit()
                break
def delete_items():
    view()
    print()
    mycursor.execute('SELECT * FROM ITEMS')
    pid=[]
    for i in mycursor:
        pid.append(i[0])
    PRODUCT_ID=input('Enter id of item to be deleted=')
    if PRODUCT_ID in pid:
        mycursor.execute("DELETE FROM ITEMS WHERE PRODUCT_ID='{}'".format(PRODUCT_ID))
        print("Item deleted successfully")
        mydb.commit()
    else:
        print('Product id does not exist')
def modify_items():
    view()
    print()
    inn=input('Enter the PRODUCT_ID of the item to be modified:')
    inn=inn.upper()
    mycursor.execute('SELECT * FROM ITEMS')
    pid=[]
    for i in mycursor:
        pid.append(i[0])
    if inn not in pid:
        print(inn,'PRODUCT ID does not exist!!!!')
    else:
        print('\nPrice (p/P)\nStock (s/S)\n')
        mod=input('What do you want to modify?(P/S):')
        mycursor.execute('SELECT * FROM ITEMS')
        al=mycursor.fetchall()
        for i in al:
            if i[0]==inn:
                if mod in ('pP'):
                    price=input('Enter the modified product price:')
                    mycursor.execute("UPDATE ITEMS \
                               SET PRODUCT_PRICE={} WHERE PRODUCT_ID={}".format(price,inn))  
                elif mod in ('Ss'):
                    aval=input('Enter the new stock:')
                    mycursor.execute("UPDATE ITEMS \
                               SET STOCK={} WHERE PRODUCT_ID={}".format(aval,inn))  
                else:
                    print('Wrong input!!!!')
                    print()
        mydb.commit()
        view()
           
def view_offers():
    print()
    print('*'*70)
    print(' '*20+'_____________OFFERS______________')
    print('*'*70)
    print()
    print('SHOP BETWEEN :')
    print('Rs.500 and Rs.1000 & get  10 sweet points.')
    print('Rs.1000 and Rs.2000 & get 30 sweet points.')
    print('Rs.2000 and Rs.3000 & get 40 sweet points.')
    print('Rs.3000 and Rs.4000 & get 50 sweet points.')
    print('Rs.4000 and 5000 & get  70  sweet points.')
    print('And 2% of the total amount if spent more than Rs.5000.')
    print('Redemption of points is allowed only when amount is greater than 500.')
    print('*'*70)
    

def report():
    dict1={}
    tot_monthly_amt=0
    tot_monthly_disc=0
    month=input('Enter the month name:')
    month=month.lower()
    m={'january':'1','february':'2','march':'3','april':'4','may':'5','june':'6','july':'7','august':'8','september':'9','october':'10','november':'11','december':'12'}
    if month in m:
        year=input('Enter year:')
        month_num=m[month]
        print()
        print('*'*70)
        print(' '*10+'_____________MONTHLY REPORT______________')
        print()
        print(' '*10+'_____________<DETAILED ORDERS>___________')
        mycursor.execute("SELECT * FROM ORDERS\
                          WHERE month(DATE_ORDERED)='{}' and year(DATE_ORDERED)='{}'".format(month_num,year))
        print('%5s'%'P_ID','%20s'%'NAME','%10s'%'SALES','%20s'%'DATE ORDERED')
        for i in mycursor:
            print('%5s'%i[0],'%20s'%i[1],'%10s'%i[2],'%20s'%i[3])
        print()
        print(' '*10+'______________<ORDERS>_____________________')
        mycursor.execute("select A.product_id,B.product_name,A.product_price,sum(B.sales),A.product_price*B.sales\
                          from items A,orders B\
                          where A.product_id=B.product_id and month(DATE_ORDERED)='{}' and year(DATE_ORDERED)='{}'\
                         group by B.product_id".format(month_num,year))
        print('%5s'%'P_ID','%20s'%'NAME','%10s'%'PRICE','%10s'%'SALES','%20s'%'TOTAL AMOUNT')

        for i in mycursor:
            tot_monthly_amt+=i[4]
            print('%5s'%i[0],'%20s'%i[1],'%10s'%i[2],'%10s'%i[3],'%20s'%i[4])
        mycursor.execute("select product_name,sum(sales)\
                         from orders\
                         where month(date_ordered)='{}' and year(date_ordered)='{}'\
                         group by product_id".format(month_num,year))
        max_num=0
        max_name=None
        for i in mycursor:
            if i[1]>max_num:
                max_num=i[1]
                max_name=i[0]

        mycursor.execute("SELECT SUM(DISCOUNT) FROM DISCOUNTS\
                        GROUP BY DATE_ORDERED HAVING MONTH(DATE_ORDERED)='{}' and YEAR(DATE_ORDERED)='{}'".format(month_num,year))    
        for i in mycursor:
            tot_monthly_disc=i[0]
        print()
        print(' '*15,'Total monthly sales: Rs',tot_monthly_amt)
        print(' '*15,'Total monthly discount: Rs',tot_monthly_disc)
        print(' '*15,'Total Revenue: Rs',tot_monthly_amt-tot_monthly_disc)
        print(' '*15,'Highest Selling Product:',max_name,':',max_num,'units')
        print('*'*70)

    else:
        print('Wrong month name!!!')        
def money_to_pts(amount,CUSTOMER_ID):
    if amount>500 and amount<=1000:
        pts=10
    elif amount>1000 and amount<=2000:
        pts=30
    elif amount>2000 and amount<=3000:
        pts=40        
    elif amount>3000 and amount<=4000:
        pts=50        
    elif amount>4000 and amount<=5000:
        pts=70       
    elif amount>5000:
        pts=amount*0.02   
    elif amount<=500:
        pts=0
    mycursor.execute("UPDATE CUSTOMERS \
                  SET CUSTOMER_POINTS=CUSTOMER_POINTS+{} where CUSTOMER_ID={}".format(pts,CUSTOMER_ID))
    mydb.commit()
    return(pts)


def pts_to_money(CUSTOMER_ID):
    mycursor.execute("SELECT * FROM CUSTOMERS\
                      WHERE CUSTOMER_ID={}".format(CUSTOMER_ID))
    record=mycursor.fetchone()
    totalpts=record[3]
    if totalpts>=200:
        discount=0.20*totalpts
    elif totalpts<200:
        discount=0
    return(totalpts,discount)

def add_customer():
    while True:
        CUSTOMER_PHNo=(input("Enter customer's phone number:"))
        if len(CUSTOMER_PHNo)==10:
            break    
        else:
            print('Invalid phone number!!!!!')
            continue 
    mycursor.execute('SELECT * FROM CUSTOMERS')
    data=mycursor.fetchall()
    found=0
    for i in data:
        if i[1]==CUSTOMER_PHNo:
            found=1
            CUSTOMER_ID=i[0]
            break
    if found==0:
        custid=[]
        for i in data:
            custid+=i[0]
        while True:
            CUSTOMER_ID=random.randint(1,1000)
            CUSTOMER_ID=str(CUSTOMER_ID)
            if CUSTOMER_ID  not in custid:
                break
        CUSTOMER_NAME=input('Enter the name of the customer:')
        CUSTOMER_NAME=CUSTOMER_NAME.title()
        points=0
        mycursor.execute("Insert into CUSTOMERS values('{}','{}','{}',{})".format(CUSTOMER_ID,CUSTOMER_PHNo,CUSTOMER_NAME,points))
    mydb.commit()
    return(CUSTOMER_ID)

def billing():
    mycursor.execute('SELECT * FROM ITEMS')
    pid=[]
    for i in mycursor:
        pid.append(i[0].lower())
    view()
    print()
    current_date=dt.date.today()
    d={}
    CUSTOMER_ID=add_customer()
    amount=0
    count=0
    tot_ids=[]
    option='y'
    while True:
        p_id=input("Enter product id=")
        if p_id in pid:
            mycursor.execute("SELECT * FROM ITEMS\
                          WHERE PRODUCT_ID='{}'".format(p_id))
            record=mycursor.fetchone()
            prod_qty=int(input('Enter product quantity='))
            prod_name=record[1]
            price=record[2]
            stock=record[3]
            d[p_id]=[prod_name,prod_qty,price]
            if stock>=prod_qty:
                count+=1
                stock=stock-prod_qty
                amount+=(price*prod_qty)
                mycursor.execute("UPDATE ITEMS \
                      SET STOCK={} where PRODUCT_ID='{}'".format(stock,p_id))
                tot_ids+=[p_id]
            elif stock==0:
                print(prod_name,'OUT OF STOCK!!')
                continue
            else:
                print('Limited Stock available for',prod_name,':',stock)
            mycursor.execute("INSERT INTO ORDERS VALUES ('{}','{}',{},'{}')".format(p_id,prod_name,prod_qty,current_date))
            
        else:
            print('Wrong product id!!!!!!!!!!')
        option=input('Would you like to enter more records?(y/n):')
        if option in 'nN':
            break
    choice='n'    
    pts=0
    totalpts,discount=pts_to_money(CUSTOMER_ID)
    if discount!=0 and amount>500:
        print('Amount is :Rs.',amount)
        print('Your Total Sweet Points are :',totalpts)
        choice=input("Would you like to redeem your points(y/n)??:")
        if choice in 'yY':
            totalpts=0
            amount-=discount
            mycursor.execute("UPDATE CUSTOMERS \
                  SET CUSTOMER_POINTS={} where CUSTOMER_id={}".format(totalpts,CUSTOMER_ID))
            mycursor.execute("INSERT INTO DISCOUNTS VALUES ('{}',{})".format(current_date,discount))
    if amount>500 and choice in 'nN':
        pts=money_to_pts(amount,CUSTOMER_ID)
        totalpts+=pts
    mycursor.execute("UPDATE CUSTOMERS \
              SET CUSTOMER_POINTS={} where CUSTOMER_id={}".format(totalpts,CUSTOMER_ID))
        
    print()
    print('*'*70)
    print('______________________CHERRY ON THE TOP CAKE SHOP______________________')
    print('*'*70)
    print()
    print()
    print('DATE : ',current_date)
    print()
    print('_______________________________________________________________________')
    print('%20s'%'DESCRIPTION','%10s'%'QTY','%10s'%'RATE','%10s'%'AMT.')
    for i in d:
        prod_price=d[i][2]
        prod_qty=d[i][1]
        final_amt=prod_price*prod_qty
        print('%20s'%d[i][0],'%10s'%d[i][1],'%10s'%d[i][2],'%10s'%final_amt)
    print()
    print('_______________________________________________________________________')

    print(' '*20,'Total amount :Rs.',amount)
    print(' '*20,'Total items : ',count)
    if choice in 'yY':
        print(' '*20,'You have saved Rs.',discount)
    print('Sweet Points rewarded : ',pts)
    print('Total sweet points : ',totalpts)
    print('*'*70)
    mydb.commit()
mydb.commit()


while True:
    print()
    print('1.View items')
    print('2.Add items')
    print('3.Delete item')
    print('4.Modify items')
    print('5.Create bill')
    print('6.View offers')
    print('7.View customer data')
    print('8.View report')
    print('9.Exit')
    print()
    print('_______________________________________________________________________')
    choice=input("Enter choice from menu=")
    if choice=='1':
        view()
    elif choice=='2':
        add_items()
    elif choice=='3':
        delete_items()
    elif choice=='4':
        modify_items()
    elif choice=='5':
        billing()
    elif choice=='6':
        view_offers()
    elif choice=='7':
        view_cust()
    elif choice=='8':
        report()
    elif choice=='9':
        print('Thankyou for using our services.')
        break
    else:
        print("Wrong input")

