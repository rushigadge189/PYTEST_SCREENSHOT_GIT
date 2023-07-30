import time

from selenium import webdriver


class Test() :
    def test_ss_001( self ) :
        driver = webdriver.Chrome() ;
        time.sleep(1) ;

        driver.implicitly_wait(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.get("https://www.credence.in/") ;
        time.sleep(1) ;

        if ( driver.title == "Credence" ) :
            driver.save_screenshot( "D:\\PYTEST_SCREENSHOT\\Screenshots\\Credence.jpeg" ) ;
            time.sleep(1) ;

            driver.close();
            assert True ;

        else :
            print ("You Are In The Wrong Place") ;
            driver.close() ;
            assert False ;

    def test_add_002 ( self ) :
        a = 2 ;
        b = 5 ;
        add = a + b ;
        print ( 'Addition Of Two Numberss = ' ,add ) ;
        if ( add == 7) :
            assert True;
        else:
            assert False ;