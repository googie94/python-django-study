# 

# dataclass
# 우리는 파이썬으로 데이터를 담기 위해 여러 방법을 사용한다.
# 나는 장고를 통해 파이썬을 처음 접했기때문에 장고식의 저장방법에 익숙하다.
# 자료 구조는 리스트 튜플 사전 네임드튜플 세트 프로즌세트 등 다양하고 사용하기 간편하다.
# 반면 클래스를 이용해 데이터를 담아두면 type이 safe해져 프로그램 실행의 오류가 적어지는 장점이 있다.

# dataclsses는 파이썬 3.7부터 라이브러리에 추가되었으며,
# 기본형은 아래와 같다. 같은 형식이 반복된다.
class User:
	def __init__(self, id: int, name: str, birthday: date, admin: bool = False) -> None:
		self.id = id
		self.name = name
		self.birthday: birthday,
		self.admin = admin

# 단점은 각 변수가 3번이나 반복해서 적히게 된다.
# 출력결과에 필드값이 나타나지 않아서 불편함도 있다.
user1 = User(id=1, name="googie", birthday=date(1994, 1, 26))
user1
# input: <__main__.User object at 0x105558100>

# __repr__() 메서드를 추가해서 필드값이 모두 추가되도록 하려면,

	def __repr__(self):
		return (
			self.__class__.__qualname__ + f"(id={self.id!r}, name={self.name!r}, "f"birthday={self.birthday!r}, admin={self.admin!r}"
		)

user2 = User(id=1, name="googie", birthday=date(1994, 1, 26))
user2
# User(id=1, name="googie", birthday=datetime.date(1994, 1, 26), admin=False)

# 위와 아래의 동등성 체크
user1 == user2
# False

# 만약 동등한 인스턴스로 취급하고 싶다면, __eq__() 메소드를 구현해줘야 합니다.
	def __eq__(self, other):
		if other.__class__ is self.__class__:
			return (slef.id, self.name, self.birthday, self.admin) == (
				other.id,
				other.name,
				ather.birthday,
				ather.admin,
			)
		return NotImplement
user1 == user2
# True



# 만약 dataclass 를 사용한다면,
# __init__(), __repr__(), __eq__()의 메소들을 자동으로 생성
# 불변의 데이터를 만들기 위해서는 'frozen=True'를 사용
# 대소비교정렬를 만들기 위해서는 'order=True'를 사용

# dataclass의 인스턴스는 기본적으로 hashable 하지 않아, 세트(set)의 값이나 사전(dict)의 키로 사용할 수 없습니다.
# 만약 hashable 하게 만들고 싶다면, 'unsafe_hash=True'를 사용
# 세트(set)를 사용해서 중복을 제거
# set([user1, user2])

# dataclass 주의사항
# 흔히 나오는 실수
from dataclasses import dataclass
from datetime import date
from typing import List
# 변경후
from dataclasses import field


@dataclass(unsafe_hash=True)
class User:
	id: int
	name: str
	birthday: date
	admin: bool = False
	# 변경 전
	friends: List[int] = [] # 기본값 할당이 불가
	# 변경 후
	friends2: List[int] = field(default_factory=list)


# 에러
# ValueError: mutable default <class 'list'> for field friends is not allowed: use default_factory
# 필드의 기본값은 인스턴스 간에 공유가 되기 때문에 이런식으로 기본값할당이 허용되지 않는다

user1 = User(id=1, name="googie", birthday=date(1994, 1, 26))
user1.friends
# []
user1.friends.append(2)
user1.friends
# [2]


# TYPING
from typing import List
nums: List[int] = [1,2,3]

from typing import Dict
countries: Dict[str, str] = {"KR": "South Korea", "US": "United States"}

from typing import Tuple
user: Tuple[int, str, bool] = (3, "googie", True)

from typing import Set
chars: Set[str] = {"A", "B", "C"}

# Final
# 재할당이 불가능한 변수, 즉 상수에 대한 타입 어노테이션을 추가할 때 사용
from typing import Final
TIME_OUT: Final[int] = 10

# Union
from typing import Union

def toString(num: Union[int, float]) -> str:
	return str(num)

toString(1)
# '1'
toString(1.5)
# '1.5'

# Optional
from typing import Optional
def repeat(message: str, times: Optional[int] = None) -> list:
	if times:
		return [message] * times
	else:
		return [message]

# Callable
# 함수를 일반값처럼 저장하거나 함수의 인자로 넘기거나 반환값으로 사용할 수 있다
# 이런 합수에 대한 타입 어노테이션을 추가할 때 사용한다



from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass(frozen=True):
class OrderLine:
	order_id: str
	sku: str
	qty: int

class Batch:
	def __init__(
		self,
		ref: str,
		sku: str,
		qty: int,
		eta: Optional[date]
	):
		self.reference = ref
		self.sku = sku
		self.eta = eta
		self.available_quantity = qty

	def allocate(self, line: OrderLine):
		self.available_quantity -= line.qty




