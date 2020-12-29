### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python uses a syntax that is more like normal english, while JS is a little less clear. Python is used for many things but not generally for front end web development like JS is.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?
A series of tests in python that test individual portions of code, often times being the functions of an application

- What is an integration test?
testing that focuses on testing parts of the code to be added to an already working application.

- What is the role of web application framework, like Flask?
To simplify and help with coding server side routes and responding to and outputing based on html requests, and various other server side needs.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
when choosing the first example you would consider if you need the whole pages content to be an example of pretzel, like it was the topic for that route. and for the second it is more likely pretzel is a small piece of the subject of that route as it is passed in an argument 

- How do you collect data from a URL placeholder parameter using Flask?
@app.route('/post/<int:post_id>'), or similar
and passing in the id as an argument into the view function.

- How do you collect data from the query string using Flask?
use request.args to pull information passed as arguments in the query string

- How do you collect data from the body of the request using Flask?
request.data or similar 

- What is a cookie and what kinds of things are they commonly used for?
sending information that will be stored in a users browser, this can sometimes be information like if they are logged in and saved preferences.

- What is the session object in Flask?
saves any given data in session or in other words till the browser is closed.

- What does Flask's `jsonify()` do?
converts python data, often dictionaries into a json string format to be recalled later.