from datetime import date, timedelta
import pytest

# from model import ...

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
	# 20개의 작은 의자가 있는 배치가 있고, 2개의 작은 의자를 요구하는 주문라인이 있다.
	# 주문 라인은 할당하면 배치에 18개가 남아야한다.

	# 20개 작은 의자가 있는 배치
	batch = Batch("batch-001", "SMALL-CHAIR", qty=20, eta=today)
	# 2개 작은 의자를 요구하는 주문라인
	line = OrderLine("order-ref", "SMALL-CHAIR", 2)

	# 배치에 주문을 할당
	batch.allocate(line)

	# assert?
	# assert [조건], [오류메시지]
	# 조건이 True일 경우 코드 진행, 아닐경우는 assert 에러메시지를 일으킨다.
	assert batch.avaliable_quantity == 18
    pytest.fail("todo")


def test_can_allocate_if_available_greater_than_required():
    pytest.fail("todo")


def test_cannot_allocate_if_available_smaller_than_required():
    pytest.fail("todo")


def test_can_allocate_if_available_equal_to_required():
    pytest.fail("todo")


def test_prefers_warehouse_batches_to_shipments():
    pytest.fail("todo")


def test_prefers_earlier_batches():
    pytest.fail("todo")
