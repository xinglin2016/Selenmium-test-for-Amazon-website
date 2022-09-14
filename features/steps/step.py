from behave import *
from searching import Searching

s = Searching()

@when('open amazon website')
def step_impl(context):
    s.land_first_page()

@then('search for {content}')
def step_impl(context, content):
    s.content_search(content)
    s.click_search()

@then('apply the filter')
def step_impl(context):
    s.apply_filtrations()

@then('add the first {num} items in cart and verify the items in the cart')
def step_impl(context, num):
    number, item_list = s.add_item_to_cart(num)
    print(f"original item list is {item_list}")
    number_cart = s.check_cart(number, item_list)
    assert number_cart == number, f"You add {number} item in the cart, but there is only {number_cart} item in the cart"

@then('close the brower')
def step_impl(context):
    s.close_page()



