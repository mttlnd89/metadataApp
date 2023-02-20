import tableauserverclient as TSC
import logging
import yaml

class apiQuery:
    
    logging.basicConfig(filename='src/app.log', filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    

    def databaseQuery():

        try:
            with open('config/dev/config.yaml','r') as file:
                config = yaml.safe_load(file)
        except Exception as error:
            logging.debug(error)

        query = """
        {
            databases
            {
                id
                name
            }
        }
            """

        tableau_auth = TSC.TableauAuth(config['user'], config['pass'], config['site'])
        server = TSC.Server(config['server'], use_server_version=True)

        dsNames = []

        with server.auth.sign_in(tableau_auth):
            resp = server.metadata.query(query)

            datasources = resp['data']['databases']

            for ds in datasources:
                dsNames.append(ds['name'])


        return list(set(dsNames))
    

    def workbookQuery(database):

        try:
            with open('config/dev/config.yaml','r') as file:
                config = yaml.safe_load(file)
        except Exception as error:
            logging.debug(error)

        query2 = """
        query ShowMeTheMoney($db:String){
            databases (filter: {name: $db})
            {
                name
                tables
                {
                name
                }
                downstreamWorkbooks{
                name
                }
            }
        }
            """
        tableau_auth = TSC.TableauAuth(config['user'], config['pass'], config['site'])
        server = TSC.Server(config['server'], use_server_version=True)

        wbNames = []
        graphqlbullshit = {'db' : database}
        print(query2)
        with server.auth.sign_in(tableau_auth):
            resp = server.metadata.query(query2,variables=graphqlbullshit)
            print('-------------------------This is the response from the metadata query:\n\n', resp, '\n\n------------------------')
#           resp = server.metadata.query(query2,variables=database)

            workbooks = resp['data']['databases']

            for wb in workbooks:
                    dsWB = wb['downstreamWorkbooks']
                    if dsWB != []:
                        tempVar = dsWB[0]
                        dsWBName = tempVar['name']
                        wbNames.append(dsWBName)


        return list(set(wbNames))

    
