import urllib.parse
import click

@click.command()
@click.option("--payload", prompt="Enter a payload...", help="Payload to encode")
def encode(payload):
    # Convert \n, \r\n, etc. into actual characters
    payload = bytes(payload, "utf-8").decode("unicode_escape")

    encoded = urllib.parse.quote(payload, safe="")
    click.echo(f"Encoded payload: {encoded}")

if __name__ == "__main__":
    encode()