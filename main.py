"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from notice import NoticeHandler
from warning import WarningHandler
from error import ErrorHandler


notice = NoticeHandler("notice")

try:
    notice.set_next(WarningHandler("warning")).set_next(ErrorHandler("error"))

    notice.execute("notice")
    notice.execute("warning")
    notice.execute("error")
except:
    print("An error occurred.")
