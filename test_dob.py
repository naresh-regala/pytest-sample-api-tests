from operator import contains
import pytest
from common import *
from datetime import datetime, timezone
import logging
import pytest


day = "day"
hour = "hour"
week = "week"
month = "month"

now = datetime.now(timezone.utc)
current_date = now.strftime("%Y-%m-%d")

class TestNextBirthday:

    @pytest.mark.regression
    def test_next_birthday_unit_day(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain days left
        """
        res = time_left_for_next_birthday("1987-07-26",day)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert 'days left' in str(res_json['message'])

    @pytest.mark.smoke
    def test_next_birthday_unit_hour(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain hours left
        """
        res = time_left_for_next_birthday("1987-07-26",hour)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert 'hours left' in str(res_json['message'])
    
    @pytest.mark.regression
    def test_next_birthday_unit_month(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain months left
        """
        res = time_left_for_next_birthday("1987-07-26",month)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert 'months left' in str(res_json['message'])

    @pytest.mark.regression
    def test_next_birthday_unit_week(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain days left
        """
        res = time_left_for_next_birthday("1987-07-26" , week)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert 'weeks left' in str(res_json['message'])
    
    @pytest.mark.regression
    def test_next_birthday_Invalid_dob_format(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain days left
        """
        res = time_left_for_next_birthday("07-26-1989" , week)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert 'Please specify dateofbirth in ISO format YYYY-MM-DD' in str(res_json['message'])

    @pytest.mark.regression
    def test_next_birthday_missing_required_params(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain days left
        """
        res = time_left_for_next_birthday("" , "")
        res_json = json.loads(res.content)
        assert res.status_code == 400, "Check status code"
        assert 'Please specify both query parameter dateofbirth and unit' in str(res_json['message'])

    @pytest.mark.regression
    def test_next_birthday_pass_current_day(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain days left
        """
        res = time_left_for_next_birthday(current_date , day)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert '0 days left' in str(res_json['message'])

    @pytest.mark.regression
    def test_next_birthday_pass_current_day_unit_hour(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain hours left
        """
        res = time_left_for_next_birthday(current_date , hour)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert '0 hours left' in str(res_json['message'])
    
    @pytest.mark.regression
    def test_next_birthday_pass_current_day_unit_week(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain weeks left
        """
        res = time_left_for_next_birthday(current_date , week)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert '0 weeks left' in str(res_json['message'])
    
    @pytest.mark.regression
    def test_next_birthday_pass_current_day_unit_month(self):
        """
        Steps.
        1. pass date of birth
        2. pass day unit
        3. response message should contain months left
        """
        res = time_left_for_next_birthday(current_date , month)
        res_json = json.loads(res.content)
        assert res.status_code == 200, "Check status code"
        assert '0 months left' in str(res_json['message'])






