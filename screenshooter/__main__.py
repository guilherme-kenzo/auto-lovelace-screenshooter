from .client import ScreenshotClient
import schedule
import click
from .schedule import run_screenshot_every



@click.command()
@click.option("--xpath", type=click.STRING, required=True, help="The XPATH of the element to be screenshot.")
@click.option("--output-file", type=click.STRING, required=True, help="The path of the output screenshot.")
@click.option("--url", type=click.STRING, required=True, help="The URL of the page you want to shoot.")
@click.option("--driver-dir", type=click.STRING, required=False, default="Directory where the driver binary is located (or is to be downloaded).")
@click.option("--every", type=click.STRING, required=False, help="Period of time between updates (in minutes or hours")
def main(**kwargs):
    run_screenshot_every(
        kwargs.get("every"),
        kwargs.get("url"),
        xpath=kwargs.get("xpath"),
        driver_dir=kwargs.get("driver_dir")
    )


if __name__ == "__main__":
    main()