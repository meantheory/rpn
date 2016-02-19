# rpn

This repo is for a RPN Calculator Exercise.

 - rpn.py implements core logic
 - test_rpn.py implements unit tests with py.test
 - api.py makes a simple web api with flask
 - calc.py is a command line interface

**Tasks**

 - [x] basic rpn implmentation
 - [x] interactive cli

**Extra Credit**

 - [x] rpn api
 - [ ] dockerize api


**Screenshot of API**

[http](https://github.com/jkbrzt/httpie) `POST 127.0.0.1:5000/v1/rpn input:='[5, 1, 2, "+", 4, "*", "+", 3, "-"]'`

![screen shot using api](https://raw.githubusercontent.com/meantheory/rpn/master/Screenshot.2016-02-19.09.08.09.png)
