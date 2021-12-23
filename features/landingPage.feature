@test-check
Feature: open lander page
    Background:
        Given launch chrome browser
        When open lander homepage


    Scenario: text presence on lander home Page
        Then verify h2 text displayed on page
        And close browser

    Scenario: Login to lander with valid parameters
        When Enter email "emilyjames202115@gmail.com" in email field
        And Click on continue button
        Then User must redirect to registration page
        And close browser