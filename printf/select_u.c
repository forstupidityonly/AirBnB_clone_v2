#include "holberton.h"
/**
  *
  */
int uhelper(unsigned int r)
{
	int count;
	unsigned int i = r;

	if (i / 10)
		uhelper(i / 10);
	count = _putchar('0' + i % 10);
	if (count == -1)
		return (count);
	return (count);
}
/**
  *
  */
int select_u(va_list args)
{
	unsigned int n = va_arg(args, unsigned int);
	unsigned int d = n;
	int count = 0;
	int r;

	if (n < 1)
	{
		_putchar('0');
		return (1);
	}
	r = uhelper(d);
	if (r == 1)
		while (d > 0)
		{
			count++;
			d /= 10;
		}
	else
		count = -1;
	return (count);
}
