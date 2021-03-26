import user_interface
from customer import Customer, check_backpack
from soda_machine import SodaMachine


def run_simulation():
    """The central method called in main.py."""
    customer = Customer()
    soda_machine = SodaMachine()
    will_proceed = True
    while will_proceed:
        user_option = user_interface.simulation_main_menu()
        if user_option == 1:
            soda_machine.begin_transaction(customer)
        elif user_option == 2:
            customer.check_coins_in_wallet()
        elif user_option == 3:
            check_backpack()
        else:
            will_proceed = False


class Simulation:
    def __init__(self):
        pass
