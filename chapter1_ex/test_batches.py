from datetime import date

def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-CAHIR", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-CHAIR", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-123', skum line_qty)
    )

