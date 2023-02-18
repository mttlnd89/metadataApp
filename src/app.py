import tableauserverclient as TSC
import logging
import yaml


def main():
    logging.basicConfig(filename='src/app.log', filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    try:
        with open('config/dev/config.yaml','r') as file:
            config = yaml.safe_load(file)
    except Exception as error:
        logging.debug(error)

    query = """
    {
        databases (filter: {name: "megaGymDataset.csv"})
        {
            id
            name
            workbooks
            {
            name
            }
        }
    }
        """
    
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

    dsNames = []

    with server.auth.sign_in(tableau_auth):
        resp = server.metadata.query(query2)
        print(resp)
'''
        datasources = resp['data']['databases']
        print(datasources)


        for ds in datasources:
            dsNames.append(ds['name'])

        for ds in dsNames:
            print(ds)
'''

if __name__ == '__main__':
    main()