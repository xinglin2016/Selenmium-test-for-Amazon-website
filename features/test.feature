Feature: search item on amazon and check result

  Scenario Outline: search Teddy bear
    When open amazon website
    Then search for <item>
    Then apply the filter
    Then add the first <num> items in cart and verify the items in the cart
    Then close the brower

    Examples:
    | item        | num |
    | Teddy bear  | 2   |