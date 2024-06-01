from zeep import Client
wsdl =  'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl)


#=================================================
#=======================List of operation available in WSDL
def ListOfOperations():
    for name, service in client.wsdl.services.items():
        print(f"Service Name:{name}")
    for port in service.ports.values():
        print(f" port: {port}")
        for operation in port.binding._operations.values():
            print(f"    Operation: {operation.name}")  # Print the operation name

               
#===================================== Invoke Operation
def Continents():
    try:
        # List of continents by name
        continents_response = client.service.ListOfContinentsByName()
        print("Continents:")
        for continent in continents_response:
            print(f"  {continent.sName} ({continent.sCode})")
    except Exception as e:
        print(f"Error: {e}")

    
#===================For Fetching data about Country Currency and its flag ingo

def getCountryCurrencyAndFlag(country_code):
    try:
        # Get country currency 
        currency_response = client.service.CountryCurrency(sCountryISOCode=country_code)
        print(f"Currency for {country_code}: {currency_response.sName} ({currency_response.sISOCode})")
        # Get country flag
        flag_response = client.service.CountryFlag(sCountryISOCode=country_code)
        print(f"Flag URL for {country_code}: {flag_response}")
        
    except Exception as e:
        print(e)
        
        
# To get list of operations avaliable is WSDL service run this function
# ListOfOperations()     

#To get list of continents available in WSDL run this function
# Continents()  

#To get the currency and flag of any country run this function
getCountryCurrencyAndFlag("US")



