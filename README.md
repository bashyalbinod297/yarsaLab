# yarsaLab
to run this test : 
  $ pytest .\tests\test_search.py --html=report.html
  here --html == report.html is to generate the html report for test results.
  
# Project Structure : 
* pageObjecct 
  * driverLocator 
      drive locater python file drive path variable
  * locator_elements
      list of location element that we are using in test case.
  * PageTile 
  Page title for assert condition required for test.
  * variables 
  
 *Tests 
  - list of test files
  
Test File Structure 
  * import required packages and library (and variables)
  * Test Class 
  * setup method
  * teardown method
  * testcase methods
