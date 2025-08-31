class Calculator:
    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        """
        Adds two numbers.

        Args:
            a (int | float): Operand a.
            b (int | float): Operand b.

        Returns:
            int | float: The sum of a and b.
        """

        raise NotImplementedError()

    @staticmethod
    def subtract(a: int | float, b: int | float) -> int | float:
        """
        Subtracts b from a.

        Args:
            a (int | float): Operand a.
            b (int | float): Operand b.

        Returns:
            int | float: The result of a - b.
        """

        raise NotImplementedError()

    @staticmethod
    def multiply(a: int | float, b: int | float) -> int | float:
        """
        Multiplies two numbers.

        Args:
            a (int | float): Operand a.
            b (int | float): Operand b.

        Returns:
            int | float: The product of a and b.
        """

        raise NotImplementedError()

    @staticmethod
    def divide(a: int | float, b: int | float) -> float:
        """
        Divides a by b.

        Args:
            a (int | float): Operand a.
            b (int | float): Operand b.

        Raises:
            ZeroDivisionError: Upon division by zero.

        Returns:
            float: The result of a / b.
        """

        raise NotImplementedError()
