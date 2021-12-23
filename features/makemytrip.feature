Feature: Make my trip search result validation
    Scenario: Validate that entered fight details are visible
        Given Open browser
        When Open make my trip url
        And Enter from
        And Select departure and return
        And Select two travellers
        Then Redirect to next page where user has validate tag text for departure