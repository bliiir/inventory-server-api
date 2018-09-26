import json
import sys

class MyApp:

    """Inventory manager

    Attributes:
        filename (str): The name of the .txt file that holds the inventory json object
        fileinfo (TYPE): # The content of the inventory file as a dict object
        path (TYPE):
        bits (TYPE): A list of path elements derived from
        method (TYPE): http request - GET, POST, PATCH or DELETE
        query (TYPE): Everything after the ? character in the HTTP request
    """

    ################## BEGIN: AUX               ##################

    # Read the file from the filename
    def filereader(self):
        _dict = {}
        with open(self.filename, 'r') as f:
            _dict = json.loads(f.read())
        return _dict

    # Write the file back to the filename - replacing it
    def filewriter(self):
        json.dump(self.fileinfo, open(self.filename, 'w'))
        return ("file updated:\n" + json.dumps(self.fileinfo, indent=4))

    # Split the HTTP path into a list of items using the character / as the delimeter
    def get_path(self):
        return self.path.split("/")

    def _is(self, path, category):
        return path == category

    def msg(self, code):
        print(code)
        msg = ["Your inventory has been updated", "No inventory here", "Your request is invalid"]
        return msg[code]

    ################## END: AUX                 ##################


    ################## BEGIN: QUERY HANDLING    ##################

    # GET - execute the HTTP GET query
    def _get(self):
        if self._is(self.loc, self.cat):
            try: return f"{self.bits[2]}: {self.fileinfo[self.bits[2]]}"
            except: return json.dumps(self.fileinfo, indent=4)
        return self.msg(1)

    # POST - execute the HTTP POST query
    def _post(self):
        if self._is(self.loc, self.cat):
            self.fileinfo[self.bits[2]] = int(self.query)
            try: return self.filewriter()
            except: return self.msg(2)

    # PATCH - execute the HTTP PATCHJ query
    def _patch(self):
        return self._post() # Since patching is the same as replacing, I am just calling the post method

    # DELETE - execute the HTTP DELETE query
    def _delete(self):
        if self._is(self.loc, self.cat):
            del self.fileinfo[self.bits[2]]
            try: return self.filewriter()
            except: return self.msg(2)

    ################## END: QUERY HANDLING      ##################


    ################## BEGIN: SETUP             ##################

    def dispatch(self, environ):
        self.filename = "inventory_api.txt"
        self.query = environ['QUERY_STRING']
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        # self.address = environ['REMOTE_ADDR'] # Not needed for this server

        self.fileinfo = self.filereader() # Get the content of the inventory file as a dict object
        self.bits = self.get_path() # Get the list of path elements

        self.loc = self.bits[1] # Store the first part of the path in self.loc
        self.cat = "inventory" # Store the category in self.cat

        if self.method == 'GET': return(self._get()) # Execute the _get method if the query method is GET
        elif self.method == 'POST': return(self._post()) # Execute the _post method if the query method is POST
        elif self.method == 'PATCH': return(self._patch()) # Execute the _patch method if the query method is PATCH
        elif self.method == 'DELETE': return(self._delete()) # Execute the _delete method if the query method is DELETE
        else: return self.msg(2)

    ################## END: SETUP               ##################






