from utils import DynamicWebScrapper as DWS

dws = DWS()

dws.set_url('https://es.khanacademy.org/exercise/prokaryotic-and-eukaryotic-cells')

print(dws.get_content())