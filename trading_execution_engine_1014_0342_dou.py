# 代码生成时间: 2025-10-14 03:42:26
import numpy as np

"""
Trading Execution Engine

This module provides a basic trading execution engine that can be used to
simulate or execute trades based on given inputs.
"""

class TradeExecutionError(Exception):
    """Custom exception for trade execution errors."""
    pass

class TradeExecutionEngine:
    """Trading Execution Engine class."""
    def __init__(self):
        """Initialize the trading execution engine."""
        self.portfolio = {}
        self.cash = 10000.0  # Starting cash

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio with the given quantity."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def execute_trade(self, symbol, quantity, price):
        """Execute a trade for the given symbol, quantity, and price."""
        if quantity <= 0:
            raise TradeExecutionError("Quantity must be positive.")
        if price <= 0:
            raise TradeExecutionError("Price must be positive.")
        if symbol not in self.portfolio:
            self.portfolio[symbol] = 0

        # Calculate the cost of the trade
        trade_cost = quantity * price

        # Check if there's enough cash for the trade
        if trade_cost > self.cash:
            raise TradeExecutionError("Insufficient cash for trade.")

        # Update portfolio and cash after trade execution
        self.portfolio[symbol] += quantity
        self.cash -= trade_cost

        # Return the updated cash and portfolio
        return self.cash, self.portfolio

    def liquidate_position(self, symbol):
        """Liquidate the position for the given symbol."""
        if symbol in self.portfolio:
            quantity = self.portfolio[symbol]
            del self.portfolio[symbol]
            return quantity
        else:
            raise TradeExecutionError("Symbol not in portfolio.")

    def get_portfolio_value(self, price_dict):
        """Calculate the total value of the portfolio based on the given prices."""
        total_value = self.cash
        for symbol, quantity in self.portfolio.items():
            if symbol in price_dict and price_dict[symbol] > 0:
                total_value += quantity * price_dict[symbol]
            else:
                raise TradeExecutionError(f"Price for {symbol} not available.")
        return total_value

    def get_portfolio_summary(self):
        """Return a summary of the current portfolio."""
        return {"cash": self.cash, "portfolio": self.portfolio}

# Example usage:
if __name__ == "__main__":
    engine = TradeExecutionEngine()
    engine.add_stock("AAPL", 10)
    engine.add_stock("GOOG", 5)
    try:
        cash, portfolio = engine.execute_trade("AAPL\, 2, 150.0)
        print("Trade Executed. Cash: ", cash)
        print("Portfolio: ", portfolio)
    except TradeExecutionError as e:
        print("Trade Execution Error: ", e)

    try:
        quantity = engine.liquidate_position("AAPL")
        print("Liquidated AAPL position. Quantity: ", quantity)
    except TradeExecutionError as e:
        print("Trade Execution Error: ", e)

    try:
        price_dict = {"AAPL": 155.0, "GOOG": 1200.0}
        portfolio_value = engine.get_portfolio_value(price_dict)
        print("Portfolio Value: ", portfolio_value)
    except TradeExecutionError as e:
        print("Trade Execution Error: ", e)
