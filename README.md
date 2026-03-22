# Inventory CLI Project

This project is a simple command-line inventory manager written in Python.
It lets the user add products, view inventory information, and calculate basic
inventory statistics.

## Current Features

- Menu with options:
  1. Add product
  2. Show result
  3. Calculate statistics
  4. Exit
- Input validation for menu option, product name, price, and quantity
- Product storage in a list of dictionaries (`inventory`)
- Basic statistics using subtotal values

## Project Files

- `main.py`: Main loop and option flow
- `menu.py`: Menu display function
- `validation_menu.py`: Input validation and product creation helpers
- `show_summary.py`: Inventory summary display

## How To Run

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

## Requirement Check

### Task 1: Conditionals and menu validation
- Status: Mostly complete
- `if`, `elif`, and `else` are used.
- Invalid options are handled and the loop continues.

### Task 2: Loop for multiple records
- Status: Complete
- The menu runs in a `while` loop until exit.
- Multiple products can be added.
- Products are stored in `inventory` as dictionaries.

### Task 3: Show all products with `for`
- Status: Partially complete
- A summary function exists and uses a `for` loop.
- It does not yet print each product in the exact required format:
  `Product: ... | Price: ... | Quantity: ...`

### Task 4: Basic statistics
- Status: Mostly complete
- Total inventory value is calculated.
- Product count is shown.

### Task 5: Documentation, comments, and function structure
- Status: Partially complete
- Code comments are now in English.
- README is now in English.
- Function structure could still be aligned more closely to:
  `agregar_producto()`, `mostrar_inventario()`, `calcular_estadisticas()`
  (or equivalent English names with same responsibilities).
