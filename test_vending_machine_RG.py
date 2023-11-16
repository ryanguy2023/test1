# Ryan Groskopf
# Student Id: 100880623
# Pytest
import pytest
from unittest.mock import Mock, patch
from vending_machine_RG import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # Create a new vending machine object
    vending = VendingMachine()

    # Add the states - ORG
    # vending.add_state(WaitingState())
    # vending.add_state(CoinsState())
    # vending.add_state(DispenseState())
    # vending.add_state(ChangeState())

    # My revisions
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())

    # Reset state to "waiting for first coin"
    vending.go_to_state('add_coins')
    assert vending.state.name == 'add_coins'

    # Test that the first coin causes a transition to 'add_coins'
    vending.event = '200'  # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200  # pennies, was .total

# Add more test cases as needed

# Run the test function
test_VendingMachine()



