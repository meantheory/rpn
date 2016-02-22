# rpn

This repo is for a RPN Calculator Exercise.

 - rpn.py implements core logic
 - rpnalt.py implements an alternate version of the rpn calculator that is more objecty
 - test_rpn.py implements unit tests with py.test
 - api.py makes a simple web api with flask
 - calc.py is a command line interface
 - shunt.py is a hacked together implementation of shunting yard algorithm - it converts 
   infix notation to postfix and runs the results through the module in rpn.py. This is 
   not pretty code and has many potential errors.

**Tasks**

 - [x] basic rpn implmentation
 - [x] interactive cli
 - [x] make an alternative implemenation
 - [x] make alternative cli

**Extra Credit**

 - [x] rpn api
 - [x] dockerize api


**Screenshot of API**

[http](https://github.com/jkbrzt/httpie) `POST 127.0.0.1:5000/v1/rpn input:='[5, 1, 2, "+", 4, "*", "+", 3, "-"]'`

![screen shot using api](https://raw.githubusercontent.com/meantheory/rpn/master/Screenshot.2016-02-19.09.08.09.png)

![2nd screen shot using api](https://raw.githubusercontent.com/meantheory/rpn/master/Screenshot%202016-02-22%2010.46.42.png)
