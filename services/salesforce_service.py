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
    # Using LineItem object and joining to parent Load
    query = """
    SELECT rtms__Load__r.Id, rtms__Load__r.Name, rtms__Load__r.rtms__Carrier_Only_Quote_Total__c
    FROM rtms__LineItem__c
    WHERE rtms__OriginCity__c = 'Chicago' AND rtms__DestinationCity__c = 'Euclid'
    ORDER BY CreatedDate DESC
    LIMIT 1
    """
    return sf.query(query)
