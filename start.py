import web
from JsonService import JsonService
from Table import Table

urls = (
  '/json', 'JsonService',
  '/table', 'Table'
)
             
if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()    
   