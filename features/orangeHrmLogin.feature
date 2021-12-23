Feature: OrangeHRM login

  Scenario Outline: Login to OrangeHRM with Multiple Parameters
    Given launch chrome browser
    When  Open HRM homepage
    And Enter username "<username>" and password  "<password>"
    And Click on login button
    Then User must succesfully login to Dashboard page
    And close browser


    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
