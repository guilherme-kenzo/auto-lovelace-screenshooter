
from multiprocessing.sharedctypes import Value
from .client import ScreenshotClient
from pprint import pprint
import schedule

def time_parser(time_string):

    def throw_format_error():
        pprint(default_error_string)
        raise ValueError(
            default_error_string
        )

    tokens = time_string.lower().split(' ')
    default_error_string = (
        "Time must be formatted as follows: {number of units} {unit (minutes or hours)}. "
        'Example: --every="3 hours"'
    )
    if len(tokens) != 2:
        throw_format_error()
    try:
        qt = int(tokens[0])
    except ValueError:
        throw_format_error()
    if tokens[1] not in ("minutes", "hours"):
        throw_format_error()
    return tokens

def run_screenshot_every(
    every_time: str,
    url: str,
    xpath: str,
    driver_dir: str,
    output_path: str,
):

    def screenshot():
        screenshot_client = ScreenshotClient(url=url, base_path=driver_dir)
        screenshot_client.take_screenshot(xpath, output_path)

    formatted_time = time_parser(every_time)
    getattr(schedule.every(formatted_time[1]), every_time).do(screenshot)