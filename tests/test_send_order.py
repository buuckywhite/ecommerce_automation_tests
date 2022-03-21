from pages.cart import Cart
from pages.checkout import Checkout

from tests.test_add_product_to_cart import test_add_product_to_cart_from_featured
from libs.helpers.generate_random_staff import *
import time


def test_send_order(browser):
    test_add_product_to_cart_from_featured(browser)
    go_checkout = Cart(browser)
    go_checkout.checkout_button.click()
    fill_checkout_data = Checkout(browser)
    fill_checkout_data.guest_checkout_radio_button.click()
    fill_checkout_data.checkout_option_continue_button.click()
    fill_checkout_data.firstname_input.input_text(random_word(6))
    fill_checkout_data.lastname_input.input_text(random_word(10))
    fill_checkout_data.email_input.input_text(random_mail(7))
    fill_checkout_data.telephone_input.input_text("1241241241")
    fill_checkout_data.company_input.input_text(random_word(15))
    fill_checkout_data.address1_input.input_text(random_word(10) + str(random_number()))
    fill_checkout_data.address2_input.input_text(random_word(5) + str(random_number()))
    fill_checkout_data.city_input.input_text(random_word(10))
    fill_checkout_data.postcode_input.input_text("12345")
    fill_checkout_data.country_select.click()
    fill_checkout_data.country_selected_from_list.click()
    fill_checkout_data.region_select.click()
    fill_checkout_data.region_selected_from_list.click()
    fill_checkout_data.billing_details_continue_button.click()
    fill_checkout_data.add_comment_input.input_text(random_word(500))
    fill_checkout_data.agreement_checkbox.click()
    fill_checkout_data.payment_method_continue_button.click()
    appeared_warning_text = fill_checkout_data.missing_payment_method_warning.text
    assert appeared_warning_text == 'Warning: Payment method required!\n×'
