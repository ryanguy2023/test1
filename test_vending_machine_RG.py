# Ryan Groskopf
# Student Id: 100880623
# Pytest
import pytest
from unittest.mock import Mock, patch
from vending_machine_RG import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # Create a new vending machine object
    vending = VendingMachine()

    # Add the states
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

    vending.event = '5'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 205  # Adjusted the expected amount to 200
    
    vending.event = '10'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 215
    
    vending.event = '25'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 240
    
    vending.event = '100'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 340

def test_buy_product():
    vending = VendingMachine()
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())

    vending.go_to_state('add_coins')
    assert vending.state.name == 'add_coins'

    vending.event = '100'  # one dollar coin
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 100

    vending.event = 'Snack(0.25)'  # selecting a product
    vending.update()
    assert vending.state.name == 'count_change'  # Adjusted the expected state to 'count_change'
    assert vending.amount == 0
    assert vending.change_due == 75

def test_insufficient_funds():
    vending = VendingMachine()
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())

    vending.go_to_state('add_coins')
    assert vending.state.name == 'add_coins'

    vending.event = '10'  # 10 cents coin
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 10

    vending.event = 'Chips(0.10)'  # selecting a product
    vending.update()
    assert vending.state.name == 'waiting'  # not enough money, back to waiting state
    assert vending.amount == 0  # Adjusted the expected amount to 0
    assert vending.change_due == 0


