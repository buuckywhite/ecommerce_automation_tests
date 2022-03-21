from pages.cart import Cart
from pages.homepage import Homepage
from pages.top_menu import TopMenu


def test_add_product_to_cart_from_featured(browser):
    add_product = Homepage(browser)
    product_name = add_product.featured_product_name.text
    add_product.add_to_cart_button.click()
    go_to_cart = TopMenu(browser)
    go_to_cart.shopping_cart_button.click()
    check_product_in_cart = Cart(browser)
    product_name_in_cart = check_product_in_cart.product_name_in_cart.text
    assert product_name == product_name_in_cart
