# Json Schema Extractor


## Description
This is a simple json schema extractor implementation in python. 
It reads the message from the json file and returns and saves the schema of the message in the `schema` folder.


## Getting Started

Setting up this project is pretty simple.
1. Clone this repo using this command 
``` 
   git clone https://github.com/Rafiatu/data2bots.git 
```

2. Change directory into `data2bots` and create a virtual environment for this project using the following command:
``` 
   python -m venv venv 
```

3. Activate the virtual environment you just created in step 2 using either of the following commands
   - On Windows: ` venv\Scripts\activate `
   - On Mac: ` source venv/bin/activate `

4. Once your virtual environment is activated, install the project's requirements by running this command in the terminal.
``` 
   pip install -r requirements.txt 
```

5. To run the main function that reads from json file and returns the schema, 
you can go into `main.py` file, and add this line of code:
``` 
   schema.extract_from_file("<insert the path to the json file whose schema you want to sniff>") 
```

6. Run the `main.py` script from the command line with the following command
``` 
   python main.py 
```
An example has been made available already in `main.py`.


## Running Tests
This project is shipped with python unittest. Running the tests is pretty straightforward.
In the terminal, run the command 
```
   python -m unittest 
```


## License

The MIT License - Copyright (c) 2022 - Rafihatu Bello
