 # Gavin's Weather App
 A weather app that uses data from the Bureau of Meterology to present data in a concise way.
 Written as a part of a school project.

 NOTE: This app is subject to change and may break at anytime!

 ## Project Description
 The weather app uses data from the Bureau of Meteorology, either through the BOM API, or through other BOM
 related sources that are JSON requests, which uses the Python Requests module to gather the data, then it
 processes the weather data into data that is easy to work with, where it is then presented in a GUI.

 The app uses Requests for API requests and PySide6 for the graphical user interface.

 Writing the backend for retrieving the weather data was the hardest part of the program, as it
 involved a lot of trial and error to see what works, as well as dealing with error handling. For
 the graphical user interface, it was designed with QT Designer, which saved a huge amount of time
 desigining the interface, allowing me to focus mainly on the backend.

 ## How to run the program

 The program was tested with Python 3.12.3, so that is the recommended version of Python to run this program.
 The program also requires that the following modules be installed in the Python environment:
 - PySide6
 - Requests
 - Dateutil
 - Ratelimit
 - PyQtGraph
 - qdarkstyle


 These modules can be installed by running the following command in the Terminal or Command Prompt:

 `python -m pip install pyside6 requests python-dateutil ratelimit pyqtgraph qdarkstyle`

 After that, the program can be run by running the "\_\_main__.py" file in the folder using Python

## Credits/Resources

This program would not be possible without a bunch of helpful sources and other projects online:

- https://github.com/tonyallan/weather-au
- https://stackoverflow.com/questions/39534018/how-to-use-bom-api-for-weather-tide-and-swell
- https://github.com/trickypr/bom-weather-docs
- https://www.pythonguis.com/pyside6-tutorial/
- https://wiki.python.org/moin/PyQt/Compass%20widget
- http://www.bom.gov.au/catalogue/data-feeds.shtml
- http://www.bom.gov.au/catalogue/anon-ftp.shtml
