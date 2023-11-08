0x06. Star Wars API

URL or Options Object: The first argument can either be a URL string, or an object of options2. Here are some of the more common options you’ll encounter in your applications2:

url: The destination URL of the HTTP request
method: The HTTP method to be used (GET, POST, DELETE, etc)
headers: An object of HTTP headers (key-value) to be set in the request
form: An object containing key-value form data
Callback Function: The second argument is a callback function that gets called when the HTTP request is completed2. This function takes three arguments:

error: Contains the error information if an error occurred during the request, otherwise null
response: Contains the response information, like status codes, headers, etc.
body: Contains the body of the response