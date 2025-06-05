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

def query_salesforce(parsed_input):
    sf = connect_salesforce()
    # Mock values - you will later parse origin/destination from `parsed_input`
    query = """
    SELECT Id, Name, rtms__Carrier_Only_Quote_Total__c FROM rtms__Load__c
    WHERE Id IN (
        SELECT rtms__Load__c FROM rtms__LineItems__r
        WHERE rtms__OriginCity__c = 'Chicago' AND rtms__DestinationCity__c = 'Euclid'
    )
    ORDER BY CreatedDate DESC
    LIMIT 1
    """
    return sf.query(query)
