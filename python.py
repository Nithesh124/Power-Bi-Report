import sqlite3
from decimal import Decimal, ROUND_HALF_UP

def get_invoices_for_client(client_name, db_path="invoices.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM invoices WHERE client_name = ?",
        (client_name,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def calculate_invoice_total(line_items, tax_rate=Decimal('0.18')):
    subtotal = sum(Decimal(str(item['amount'])) for item in line_items)
    total = subtotal * (Decimal('1') + tax_rate)
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def apply_bulk_discount(invoices, discount_percent):
    discount = Decimal(str(discount_percent))  # avoid float precision bugs
    for invoice in invoices:
        invoice['total'] -= (invoice['total'] * discount / Decimal('100'))
        invoice['total'] = invoice['total'].quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return invoices