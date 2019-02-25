class OPSResponse:
    __slots__ = ['status_code', 'json', 'log_message', 'success', 'error']
    def __init__(self, status_code=None, json=None, log_message=None, success=None, error=None):
        if status_code is None:
            status_code = 0
        self.status_code = status_code
        if json is None:
            json = { 'none' : None }
        self.json = json
        if log_message is None:
            log_message = "Unknown error occured."
        self.log_message = log_message
        if success is None:
            success = False
        self.success = success
        if error is None:
            error = "Unknown"
        self.error = error

    def wasSuccessful(self,message):
        self.success = True
        self.error = "No error"
        self.log_message = message

    def failed(self,errorName, message):
        self.success = False
        self.error = errorName
        self.log_message = message

    def setJson(self,json):
        self.json = json


    def setStatusCode(self,status_code,requestType=""):
        #
            # The following API responses are from: http://docs.octoprint.org/en/master/api/index.html as of 2/20/2019
            # POST /api/login - http://docs.octoprint.org/en/master/api/general.html#post--api-login
            #   -   200 OK - Successful login
            #   -   NA because logging in with API key (401 Unauthorized - Username/password mismatch or unknown user)
            #   -   403 Forbidden - Deactivated account (or incorrect API key)

            # POST /api/logout - http://docs.octoprint.org/en/master/api/general.html#post--api-logout
            #   -   204 No Content - No error

            # GET /api/connection - http://docs.octoprint.org/en/master/api/connection.html#get--api-connection
            #   -   200 OK - No error
            # POST /api/connection - http://docs.octoprint.org/en/master/api/connection.html#post--api-connection
            #   -   204 No Content - No error
            #   -   400 Bad Request - If the selected port or baudrate for a connect command are not part of the available options.

            # GET /api/printer - http://docs.octoprint.org/en/master/api/printer.html#get--api-printer
            #   -   200 OK - No error
            #   -   409 Conflict - If the printer is not operational.

            # POST /api/printer/tool - http://docs.octoprint.org/en/master/api/printer.html#post--api-printer-tool
            #   -   204 No Content - No error
            #   -   400 Bad Request - If targets or offsets contains a property or tool contains a value not matching the format tool{n}, the target/offset temperature, extrusion amount or flow rate factor is not a valid number or outside of the supported range, or if the request is otherwise invalid.
            #   -   409 Conflict - If the printer is not operational or 
            # NA FOR INDIGO PLUGIN (- in case of select or extrude - currently printing).

            # POST /api/printer/bed - http://docs.octoprint.org/en/master/api/printer.html#post--api-printer-bed
            #   -   204 No Content - No error
            #   -   400 Bad Request - If target or offset is not a valid number or outside of the supported range, or if the request is otherwise invalid.
            #   -   409 Conflict - If the printer is not operational or 
            # NA FOR ME ONLY(the selected printer profile does not have a heated bed).
            # ^!Will need to implement heated bed check in octoPrintService and disable sending bed target commands accordingly. See GET /api/printerprofiles below!^ 

            # GET /api/printerprofiles - http://docs.octoprint.org/en/master/api/printerprofiles.html#get--api-printerprofiles
            #   -   200 OK - No error

        self.status_code = status_code
        if status_code >= 200 and status_code < 300:
            self.success = True
            self.error = "No error"
            self.log_message = "API successfully processed request: {0}".format(requestType)
            if requestType == "login":
                self.log_message = "Successful login"
           
        elif status_code >=400:
            self.success = False
            
            if status_code == 400:
                self.error = "Bad Request"
                if requestType == "connection":
                    self.log_message = "The selected port or baudrate are not part of the available options."

                elif requestType == "tool":
                    self.log_message = "\"targets\" contains a property or \"tool\" contains a value not matching the format: \"tool(n)\", or the target temperature is not a valid number or is outside of the supported range, or the request is otherwise invalid."

                elif requestType == "bed":
                    self.log_message = "Target temperature is not a valid number or is outside of the supported range, or the request is otherwise invalid."

                else:
                    self.log_message = "The request is invalid, or an unrecognized \"requestType\" was passed to \"setStatusCode()\""

            elif status_code == 403:
                self.error = "Forbidden"
                self.log_message = "Deactivated account or incorrect API key."

            elif status_code == 404:
                self.error = "Not Found"
                self.log_message = "OctoPrint API not running on hostname/ip."

            elif status_code == 409:
                self.error = "Conflict"
                self.log_message = "The printer is not operational."

            elif status_code == 598:
                self.error = "Connection Error"
                self.log_message = "\"requests\" raised a \"ConnectionError\" exception. OctoPrint API may not be not running on hostname/ip."

            elif status_code == 599: 
                self.error = "Request Timeout"
                self.log_message = "OctoPrint API took too long to respond. OctoPrint API may not be not running on hostname/ip."





