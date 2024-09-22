import requests
from myapp.models import Address, ClassificationInsType, ClassificationProdType, ClosedAccount, ConsCommDetails

def fetch_and_store_data():
    url = 'https://webserver.creditreferencenigeria.net/JsonLiveRequest/JsonService.svc/CIRRequest/ProcessRequestJson'
    headers = {
        'Content-Type': 'application/json',
        'UserName': '28934847orosca',
        'Password': 'te3tYdgeg654@2023'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            print("Error decoding JSON response")
            return

        # Process and store data into Django models
        for item in data.get('addresses', []):
            Address.objects.create(
                address=item['ADDRESS'].strip(),
                addr_type=item['ADDR_TYPE'],
                date_reported=item['DATE_REPORTED'],
                sno=item['SNO']
            )

        for item in data.get('ClassificationInsType', []):
            ClassificationInsType.objects.create(
                amount_overdue=item['AMOUNT_OVERDUE'].strip(),
                approved_credit_sanctioned=item['APPROVED_CREDIT_SANCTIONED'].strip(),
                currency=item['CURRENCY'],
                institution_type=item['INSTITUTION_TYPE'],
                legal_flag=item['LEGAL_FLAG'],
                no_of_accounts=item['NO_OF_ACCOUNTS'],
                outstanding_balance=item['OUSTANDING_BALANCE'].strip()
            )

        for item in data.get('ClassificationProdType', []):
            ClassificationProdType.objects.create(
                amount_overdue=item['AMOUNT_OVERDUE'].strip(),
                currency=item['CURRENCY'],
                no_acc_last_six_mon=item['NO_ACC_LAST_SIX_MON'],
                no_of_accounts=item['NO_OF_ACCOUNTS'],
                product_type=item['PRODUCT_TYPE'],
                sanctioned_amount=item['SANCTIONED_AMOUNT'].strip(),
                total_outstanding_balance=item['TOTAL_OUTSTANDING_BALANCE'].strip()
            )

        if 'ClosedAccounts' in data:
            closed_account = data['ClosedAccounts']['ClosedAccounts']
            ClosedAccount.objects.create(
                account_status=closed_account['ACCOUNT_STATUS'],
                cf_closing_date=closed_account['CF_CLOSING_DATE'],
                credit_facility_type=closed_account['CREDIT_FACILITY_TYPE'],
                currency=closed_account['CURRENCY'],
                institution_name=closed_account['INSTITUTION_NAME'],
                legal_action_status=closed_account['LEGAL_ACTION_STATUS'],
                sanction_amount=closed_account['SANCTION_AMOUNT'].strip(),
                sno=closed_account['SNO']
            )

        for item in data.get('ConsCommDetails', {}).get('ConsCommDetails_ID', []):
            ConsCommDetails.objects.create(
                expiry_date=item['EXPIRY_DATE'],
                identifier_number=item['IDENTIFIER_NUMBER'],
                id_type=item['ID_TYPE']
            )
    else:
        print(f"Error fetching data: {response.status_code}")
