import pytest
from Base.base import Base


@pytest.mark.usefixtures('set_up')
class TestTitle(Base):

    def test_title_text(self):
        driver = self.driver
        assert 'The Internet' in driver.title
        assert "The Internet 1" not in driver.title
