import mock
import datetime
from pyma_module import time_diff
from pyma_module import mini_game
from pyma_module import Pet

time1 = datetime.datetime(2019, 11, 12, 5, 30)
time2 = datetime.datetime(2019, 11, 12, 5, 29)
time_delta_change_health = datetime.timedelta(seconds = 20)
time_delta_change_happiness = datetime.timedelta(seconds = 200)
test_time1 = datetime.datetime.now() - time_delta_change_health
test_time2 = datetime.datetime.now() - time_delta_change_happiness

time_diff_expected_output = 60

def test_time_diff():
	'''tests time_diff function'''
	assert callable(time_diff)
	assert time_diff(time1, time2) == time_diff_expected_output


status_list = [1, 2, 3]
def test_mini_game():
	'''tests mini_game function'''
	assert callable(time_diff)
	with mock.patch('builtins.input', return_value="scissors"):
		assert mini_game("") in status_list

#initialize a Pet
test_pet = Pet()

def test_update_health():
	'''tests update_health method'''
	assert callable(test_pet.update_health)
	test_pet.update_health(test_time1)
	health2 = test_pet.health

	assert health2 == 99

def test_update_happiness():
	'''tests update_happiness method'''
	assert callable(test_pet.update_happiness)
	test_pet.update_happiness(test_time2)
	happiness2 = test_pet.happiness

	assert happiness2 == 4
