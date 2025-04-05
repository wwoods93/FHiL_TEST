



class fhil_test:

    # class variables for tracking resources
    # class variables for keeping track of tests




    # how test works
    #
    # on start up
    #
    # user runs app
    #
    # app init
    #
    #   find/verify directory/file locations
    #   set up debug/meta data logging
    #       check packages, versions, etc.
    #   set up (test) data manager
    #   establish connection to mux board
    #   run mux self test
    #   check for list of known instruments
    #       attempt ping/connection
    #       display connections made
    #
    #   check for loaded test files
    #       display available tests or no test files loaded
    #
    #   allow user to start one or more tests
    #
    #
    #
    # test run
    #
    #   verify test parameters
    #   acquire instruments
    #   set instruments to default state
    #   verify correct DUT connected -> need ID lines for DUT
    #   start test
    #
    #       test step
    #           configure mux array and verify
    #           configure instruments and verify
    #           execute test step
    #           clean up test step
    #       repeat for additional steps
    #       clean up test
    #   end test
    #
    # COUNter commands
    #