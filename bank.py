# import streamlit as st
# all_accounts=[]
# import random

# if 'all_accounts' not in st.session_state:
#     st.session_state.all_accounts = []
# #function to open account
# def open_account(cnic, title, initial_deposit):
#     account = {'cnic'            :cnic,
#                'title'           :title,
#                'balance'         :initial_deposit,
#                'account_number'  :random.randint(1001,9999),
#                'pin'             :random.randint(1001,9999)
#     }
#     st.session_state.all_accounts.append(account)
#     #return f"""Your account has successfully created
#             #   Your account number is {account['account_number']}
#                #Your pin is {account['pin']} """
#     return account
# #function to check balance
# def check_balance(account, pin):
#     for acc in st.session_state.all_accounts :
#         if acc['account_number']==account:
#             if acc['pin']==pin:
#                 return acc['balance']
#             else:
#                 return "Invalid Pin"
#     else:
#         return "Invalid Account Number"

# #function to withdraw amount
# def withdraw(account, pin, amt):
#     for acc in st.session_state.all_accounts :
#         if acc['account_number']==account:
#             if acc['pin']==pin:
#                 if acc['balance']>=amt:
#                     acc['balance']-=amt
#                     return acc['balance']
#                 else:
#                     return "Insufficient Amount"
#             else:
#                 return "Invalid Pin"

#     else:
#         return "Invalid Account Number"
#  #function to deposit amount   
# def deposit(account,amt):
#     for acc in st.session_state.all_accounts :
#         if acc['account_number']==account:
#             acc['balance']+=amt
#             return  acc['balance']
#     else:
#         return "Invalid Account Number"
    
# #function to transfer amount
# def transfer(account, pin, amt, bacc):
#     for ba in st.session_state.all_accounts :
#         if ba['account_number'] == bacc:
#             for acc in st.session_state.all_accounts:
#                 if acc['account_number'] == account:

#                     if acc['pin'] == pin:
#                         if acc['balance'] >= amt:
#                             ba['balance'] += amt
#                             acc['balance'] -= amt
#                             return acc['balance']
#                         else:
#                             return "Insufficient Amount"
#                     else:
#                         return "Invalid Pin"
#             else:
#                 return "Invalid Account Number"
#     else:
#         return "Invalid Beneficiary Account Number"

# #function to close account
# closed_account = []
# def close_account(account, pin):
#     for acc in st.session_state.all_accounts :
#         if acc['account_number']==account:
#             if acc['pin']==pin:
#                 closed_account.append(all_accounts.pop(all_accounts.index(acc)))
#                 return acc
#             else:
#                 return "Invalid Pin"
#         else:
#             return "Invalid Account Number"
# def change_pin(account, pin, new_pin):
#     for acc in st.session_state.all_accounts :
#         if acc['account_number']==account:
#             if acc['pin']==pin:
#                 acc['pin']=new_pin
#                 return acc
#             else:
#                 return "Invalid Pin"
#         else:
#             return "Invalid Account Number"

# def show_all_accounts():
#     return st.session_state.all_accounts

# st.title("Simple bank system")
# st.write("this is a simple banking system built using streamlit")

# menu=st.sidebar.selection(
#     "Select Action"
#     [
#     "open account","close accountt","check balance","deposite","withdraw","showallacount"
#     ]
# )


import streamlit as st
import random

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Simple Bank System",
    page_icon="🏦",
    layout="wide"
)

# ================= SESSION STATE =================

if "all_accounts" not in st.session_state:
    st.session_state.all_accounts = []


# ================= HELPER FUNCTION =================

def find_account(account_number):
    for acc in st.session_state.all_accounts:
        if acc["account_number"] == account_number:
            return acc
    return None


# ================= OPEN ACCOUNT =================

def open_account(cnic, title, initial_deposit):

    for acc in st.session_state.all_accounts:
        if acc["cnic"] == cnic:
            return "CNIC already registered"

    account_number = random.randint(100000, 999999)

    while find_account(account_number):
        account_number = random.randint(100000, 999999)

    pin = random.randint(1000, 9999)

    account = {
        "cnic": cnic,
        "title": title,
        "balance": initial_deposit,
        "account_number": account_number,
        "pin": pin
    }

    st.session_state.all_accounts.append(account)

    return account


# ================= CHECK BALANCE =================

def check_balance(account_number, pin):

    acc = find_account(account_number)

    if acc is None:
        return "Invalid Account Number"

    if acc["pin"] != pin:
        return "Invalid PIN"

    return acc["balance"]


# ================= DEPOSIT =================

def deposit(account_number, pin, amount):

    acc = find_account(account_number)

    if acc is None:
        return "Invalid Account Number"

    if acc["pin"] != pin:
        return "Invalid PIN"

    if amount <= 0:
        return "Amount must be greater than zero"

    acc["balance"] += amount

    return acc["balance"]


# ================= WITHDRAW =================

def withdraw(account_number, pin, amount):

    acc = find_account(account_number)

    if acc is None:
        return "Invalid Account Number"

    if acc["pin"] != pin:
        return "Invalid PIN"

    if amount <= 0:
        return "Amount must be greater than zero"

    if acc["balance"] >= amount:
        acc["balance"] -= amount
        return acc["balance"]

    return "Insufficient Balance"


# ================= TRANSFER =================

def transfer(account_number, pin, amount, beneficiary):

    sender = find_account(account_number)
    receiver = find_account(beneficiary)

    if sender is None:
        return "Invalid Sender Account"

    if receiver is None:
        return "Invalid Beneficiary Account"

    if sender["pin"] != pin:
        return "Invalid PIN"

    if account_number == beneficiary:
        return "Cannot transfer to your own account"

    if amount <= 0:
        return "Amount must be greater than zero"

    if sender["balance"] < amount:
        return "Insufficient Balance"

    sender["balance"] -= amount
    receiver["balance"] += amount

    return sender["balance"]


# ================= CLOSE ACCOUNT =================

def close_account(account_number, pin):

    acc = find_account(account_number)

    if acc is None:
        return "Invalid Account Number"

    if acc["pin"] != pin:
        return "Invalid PIN"

    if acc["balance"] != 0:
        return "Please withdraw your remaining balance first"

    st.session_state.all_accounts.remove(acc)

    return "Account Closed Successfully"


# ================= SHOW ALL ACCOUNTS =================

def show_all_accounts():

    accounts = []

    for acc in st.session_state.all_accounts:

        accounts.append({
            "Account Number": acc["account_number"],
            "Account Title": acc["title"],
            "Balance": acc["balance"]
        })

    return accounts


# ================= MAIN PAGE =================

st.title("🏦 Simple Bank System")

st.write("Welcome to our Simple Banking Application!")

st.sidebar.title("Bank Menu")

menu = st.sidebar.selectbox(
    "Select Action",
    [
        "Open Account",
        "Close Account",
        "Check Balance",
        "Deposit",
        "Withdraw",
        "Transfer",
        "Show All Accounts"
    ]
)


# ================= OPEN ACCOUNT =================

if menu == "Open Account":

    st.header("📝 Open New Account")

    with st.form("open_form"):

        cnic = st.text_input(
            "Enter CNIC",
            placeholder="4210112345671"
        )

        title = st.text_input(
            "Account Title",
            placeholder="Enter your full name"
        )

        initial_deposit = st.number_input(
            "Initial Deposit",
            min_value=0.0,
            step=500.0
        )

        submit = st.form_submit_button("Create Account")

        if submit:

            clean_cnic = cnic.replace("-", "").strip()

            if not clean_cnic.isdigit() or len(clean_cnic) != 13:
                st.error("Enter a valid 13-digit CNIC")

            elif not title.strip():
                st.error("Account title is required")

            else:

                result = open_account(
                    clean_cnic,
                    title.strip(),
                    initial_deposit
                )

                if isinstance(result, dict):

                    st.success("Account Created Successfully!")

                    st.write("Account Title:", result["title"])
                    st.write("Account Number:", result["account_number"])
                    st.write("Your PIN:", result["pin"])

                    st.warning(
                        "Save your account number and PIN securely."
                    )

                else:
                    st.error(result)


# ================= CHECK BALANCE =================

elif menu == "Check Balance":

    st.header("💰 Check Account Balance")

    with st.form("balance_form"):

        account_number = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        pin = st.number_input(
            "Enter PIN",
            min_value=1000,
            max_value=9999,
            step=1
        )

        submit = st.form_submit_button("Check Balance")

        if submit:

            result = check_balance(account_number, pin)

            if isinstance(result, (int, float)):
                st.success(f"Your Balance: Rs. {result:,.2f}")
            else:
                st.error(result)


# ================= DEPOSIT =================

elif menu == "Deposit":

    st.header("➕ Deposit Money")

    with st.form("deposit_form"):

        account_number = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        pin = st.number_input(
            "Enter PIN",
            min_value=1000,
            max_value=9999,
            step=1
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=500.0
        )

        submit = st.form_submit_button("Deposit Money")

        if submit:

            result = deposit(account_number, pin, amount)

            if isinstance(result, (int, float)):
                st.success(
                    f"Deposit Successful! New Balance: Rs. {result:,.2f}"
                )
            else:
                st.error(result)


# ================= WITHDRAW =================

elif menu == "Withdraw":

    st.header("➖ Withdraw Money")

    with st.form("withdraw_form"):

        account_number = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        pin = st.number_input(
            "Enter PIN",
            min_value=1000,
            max_value=9999,
            step=1
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=500.0
        )

        submit = st.form_submit_button("Withdraw Money")

        if submit:

            result = withdraw(account_number, pin, amount)

            if isinstance(result, (int, float)):
                st.success(
                    f"Withdrawal Successful! Remaining Balance: Rs. {result:,.2f}"
                )
            else:
                st.error(result)


# ================= TRANSFER =================

elif menu == "Transfer":

    st.header("🔄 Transfer Money")

    with st.form("transfer_form"):

        account_number = st.number_input(
            "Your Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        pin = st.number_input(
            "Your PIN",
            min_value=1000,
            max_value=9999,
            step=1
        )

        beneficiary = st.number_input(
            "Beneficiary Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        amount = st.number_input(
            "Transfer Amount",
            min_value=0.0,
            step=500.0
        )

        submit = st.form_submit_button("Transfer Money")

        if submit:

            result = transfer(
                account_number,
                pin,
                amount,
                beneficiary
            )

            if isinstance(result, (int, float)):
                st.success(
                    f"Transfer Successful! Remaining Balance: Rs. {result:,.2f}"
                )
            else:
                st.error(result)


# ================= CLOSE ACCOUNT =================

elif menu == "Close Account":

    st.header("❌ Close Bank Account")

    with st.form("close_form"):

        account_number = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )

        pin = st.number_input(
            "Enter PIN",
            min_value=1000,
            max_value=9999,
            step=1
        )

        submit = st.form_submit_button("Close Account")

        if submit:

            result = close_account(account_number, pin)

            if result == "Account Closed Successfully":
                st.success(result)
            else:
                st.error(result)


# ================= SHOW ALL ACCOUNTS =================

elif menu == "Show All Accounts":

    st.header("👥 All Bank Accounts")

    accounts = show_all_accounts()

    if accounts:

        st.dataframe(
            accounts,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "Total Accounts",
            len(accounts)
        )

    else:

        st.info("No Accounts Available Yet!")


# ================= FOOTER =================

st.sidebar.divider()
st.sidebar.caption("Simple Bank System | Python + Streamlit")





