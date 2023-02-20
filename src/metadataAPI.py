import tableauserverclient as TSC
import logging
import yaml

class apiQuery:
    
    logging.basicConfig(filename='src/app.log', filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    

    def databaseQuery(self):

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
    

    def workbookquery():

        try:
            with open('config/dev/config.yaml','r') as file:
                config = yaml.safe_load(file)
        except Exception as error:
            logging.debug(error)

        query2 = """
        {
            databases (filter: {name: "megaGymDataset.csv"})
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

        with server.auth.sign_in(tableau_auth):
            resp = server.metadata.query(query2)
            print(resp)

            workbooks = resp['data']['databases']
            print(workbooks)


            for wb in workbooks:
                wbNames.append(wb['name'])

            print(wbNames)

        return list(set(wbNames))

    
