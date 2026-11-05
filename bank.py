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

st.title("Simple bank system")
st.write("this is a simple banking system built using streamlit")

menu=st.sidebar.selection(
    "Select Action"
    [
    "open account","close accountt","check balance","deposite","withdraw","showallacount"
    ]
)





