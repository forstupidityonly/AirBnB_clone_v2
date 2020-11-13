#include "holberton.h"
/**
  *
  */
int select_r(va_list args)
{
	char *string = va_arg(args, char *);
	int len = _strlen(string) - 1;
	int count = 0;

	while (len >= 0)
	{
		_putchar(*(string + len));
		len--;
		count++;
	}
	return (count);
}
