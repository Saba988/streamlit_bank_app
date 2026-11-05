import streamlit as st
all_accounts=[]
import random

if 'all_accounts' not in st.session_state:
    st.session_state.all_accounts = []
#function to open account
def open_account(cnic, title, initial_deposit):
    account = {'cnic'            :cnic,
               'title'           :title,
               'balance'         :initial_deposit,
               'account_number'  :random.randint(1001,9999),
               'pin'             :random.randint(1001,9999)
    }
    st.session_state.all_accounts.append(account)
    #return f"""Your account has successfully created
            #   Your account number is {account['account_number']}
               #Your pin is {account['pin']} """
    return account
#function to check balance
def check_balance(account, pin):
    for acc in st.session_state.all_accounts :
        if acc['account_number']==account:
            if acc['pin']==pin:
                return acc['balance']
            else:
                return "Invalid Pin"
    else:
        return "Invalid Account Number"

#function to withdraw amount
def withdraw(account, pin, amt):
    for acc in st.session_state.all_accounts :
        if acc['account_number']==account:
            if acc['pin']==pin:
                if acc['balance']>=amt:
                    acc['balance']-=amt
                    return acc['balance']
                else:
                    return "Insufficient Amount"
            else:
                return "Invalid Pin"

    else:
        return "Invalid Account Number"
 #function to deposit amount   
def deposit(account,amt):
    for acc in st.session_state.all_accounts :
        if acc['account_number']==account:
            acc['balance']+=amt
            return  acc['balance']
    else:
        return "Invalid Account Number"
    
#function to transfer amount
def transfer(account, pin, amt, bacc):
    for ba in st.session_state.all_accounts :
        if ba['account_number'] == bacc:
            for acc in st.session_state.all_accounts:
                if acc['account_number'] == account:

                    if acc['pin'] == pin:
                        if acc['balance'] >= amt:
                            ba['balance'] += amt
                            acc['balance'] -= amt
                            return acc['balance']
                        else:
                            return "Insufficient Amount"
                    else:
                        return "Invalid Pin"
            else:
                return "Invalid Account Number"
    else:
        return "Invalid Beneficiary Account Number"

#function to close account
closed_account = []
def close_account(account, pin):
    for acc in st.session_state.all_accounts :
        if acc['account_number']==account:
            if acc['pin']==pin:
                closed_account.append(all_accounts.pop(all_accounts.index(acc)))
                return acc
            else:
                return "Invalid Pin"
        else:
            return "Invalid Account Number"
def change_pin(account, pin, new_pin):
    for acc in st.session_state.all_accounts :
        if acc['account_number']==account:
            if acc['pin']==pin:
                acc['pin']=new_pin
                return acc
            else:
                return "Invalid Pin"
        else:
            return "Invalid Account Number"

def show_all_accounts():
    return st.session_state.all_accounts 

# Interface to user using streamlit
st.title("ðŸ¦ Simple Banking System")
st.write("This is a simple banking system built using Streamlit.")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Close Account","Check Balance", "Deposit", "Withdraw", "Transfer", "Show All Accounts"]
)

if menu == "Open Account":
    st.header("âž• Open a New Account")

    cnic = st.text_input("Enter CNIC")
    title = st.text_input("Account Title")
    deposit = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create Account"):
        acc = open_account(cnic, title, deposit)
        st.success("Account Created Successfully!")
        st.write(f"**Account Number:** {acc['account_number']}")
        st.write(f"**PIN:** {acc['pin']} (Save this!)")
        
if menu == "Close Account":
    st.header("âž– Close an Account")

    account = st.number_input("Enter Account Number")
    pin = st.number_input("Enter PIN")

    if st.button("Close Account"):
        acc = close_account(account, pin)
        st.success(acc)
        
        
if menu == "change pin":
    st.header("ðŸ”‘ Change PIN")
    account = st.number_input("Enter Account Number")
    pin = st.number_input("Enter Current PIN")
    new_pin = st.number_input("Enter New PIN")
    
    if st.button("Change PIN"):
        acc = change_pin(account, pin, new_pin)
        st.success(acc)


if menu == "Check Balance":
    st.header("ðŸ’µ Check Balance")
    account = st.number_input("Enter Account Number", min_value=0)
    pin = st.number_input("Enter PIN")

    if st.button("Check Balance"):
        balance = check_balance(account, pin)
        st.success(f"Your current balance is: {balance}")
        
if menu == "Deposit":
    st.header("ðŸ’° Deposit Money")

    account = st.number_input("Enter Account Number", min_value=0)
    amt = st.number_input("Enter Amount to Deposit", min_value=0)

    if st.button("Deposit"):
        balance = deposit(account, amt)
        st.success(balance)
        
if menu == "Withdraw":
    st.header("ðŸ’¸ Withdraw Money")

    account = st.number_input("Enter Account Number")
    pin = st.number_input("Enter PIN")
    amt = st.number_input("Enter Amount to Withdraw", min_value=0)

    if st.button("Withdraw"):
        balance = withdraw(account, pin, amt)
        st.success(balance)
        
if menu == "Transfer":
    st.header("ðŸ”„ Transfer Money")

    account = st.number_input("Enter Your Account Number", min_value=0)
    pin = st.number_input("Enter Your PIN", min_value=0)
    amt = st.number_input("Enter Amount to Transfer", min_value=0)
    bacc = st.number_input("Enter Beneficiary Account Number", min_value=0)

    if st.button("Transfer"):
        balance = transfer(account, pin, amt, bacc)
        st.success(balance)
        
if menu == "Show All Accounts":
    st.header("ðŸ“‹ All Accounts")
    if st.button("Show Accounts"):
        acc = show_all_accounts()
        st.write(acc)
    





print(all_accounts)
