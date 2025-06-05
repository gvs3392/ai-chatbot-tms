from simple_salesforce import Salesforce
import os

def connect_salesforce():
    return Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token="",
        client_id=os.getenv("SF_CLIENT_ID"),
        domain="login"
    )

def query_salesforce(origin, destination):
    sf = connect_salesforce()
    query = f"""
    SELECT Id, Name, rtms__Carrier_Only_Quote_Total__c
    FROM rtms__Load__c
    WHERE rtms__Origin__c LIKE '{origin}%' AND rtms__Destination__c LIKE '{destination}%'
    ORDER BY CreatedDate DESC
    LIMIT 1
    """
    return sf.query(query)
