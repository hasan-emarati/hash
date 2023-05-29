# import click

# @click.group()
# def cli():
#     pass

# @click.command()
# def function1():
#     # Code for function 1
#     click.echo('Function 1 is running')

# @click.command()
# def function2():
#     # Code for function 2
#     click.echo('Function 2 is running')

# cli.add_command(function1)
# cli.add_command(function2)

# if __name__ == '__main__':
#     cli()









# import click

# @click.command()
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def function1(name):
#     """Greet someone."""
#     click.echo(f'Hello, {name}!')

# @click.command()
# @click.option('--num', prompt='Enter a number', help='A number to square.')
# def function2(num):
#     """Square a number."""
#     result = int(num) ** 2
#     click.echo(f'{num} squared is {result}')

# if __name__ == '__main__':
#     function1()
#     function2()








import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('text')
def hash_search(text):
    """
    Search in hash.
    """
    click.echo(f"Searching text: {text}")

@cli.command()
def pass_to_hash():
    """
    Translate password list to hash.
    """
    click.echo("Translating password list to hash...")

@cli.command()
@click.argument('value')
def set_value(value):
    """
    Set value.
    """
    click.echo(f"Value set to {value}.")

if __name__ == '__main__':
    cli()