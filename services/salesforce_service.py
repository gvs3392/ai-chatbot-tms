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
    # Partial match using LIKE to support city-only user input
    query = """
    SELECT Id, Name, rtms__Carrier_Only_Quote_Total__c
    FROM rtms__Load__c
    WHERE rtms__Origin__c LIKE 'Chicago%' AND rtms__Destination__c LIKE 'Euclid%'
    ORDER BY CreatedDate DESC
    LIMIT 1
    """
    return sf.query(query)
