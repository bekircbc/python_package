# cebrify

![cebrify](Cebrify.png)

- Cebrify is a small npm package for calculating some features.

- Install cebrify with the following command

        python install cebrify

- Create a index.py file and add the following code for using cebrify.

        from cebrify import maxFinder, minFinder, csvReader

- Cebrify has this functions available.

        maxFinder
        minFnder
        csvReader

## maxFinder and minFinder

- Write the following code.

        list=[30,-20,30,-45]
        maxFinder(list)
        minFinder(list)

## csvReader

- add data folder and put in it a data.csv file

- Write the following code

        csvReader(./data/data.csv)

# creating python package

- create functions.py

        def calcAverage(*list):
           for line in list:
              sum+=line
           average = sum/list.lenght
        return average

- create **init**.py

        from .functions import calcAverage

- create setup.py

        from setuptools import setup
        setup(name='cebrify',
        version='0.1',
        description='A small package for calculating some features and reading files data',
        url='#',
        author='bekircbc',
        author_email='b.burakcebecii@gmal.com',
        license='MIT',
        packages=['cebrify'],
        zip_safe=False)

## for publishing this package

        pip install mypackage
