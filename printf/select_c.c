#include "holberton.h"
/**
  * select_c - print char
  * @args: the args
  * Return: num of char printed
  */
int select_c(va_list args)
{
	char c = va_arg(args, int);

	_putchar(c);
	return (1);
}
