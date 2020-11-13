#include "holberton.h"
/**
  * _printf - small printf function
  * @format: is a character string. The format string is
  * composed of zero or more directives.
  * Return: count
  *
  * print until % is found if %% put %
  * found char after % check if its null bit
  * its not so found format specifier after %
  * find correct formatting function
  * call function to print and track count
  * function should be a function ptr
  * get_func - takes in format specifier and returns ptr to correct func
  * and return count of printed values
  */
int _printf(const char *format, ...)
{
	int count = 0;
	va_list args;
	int (*function)(va_list);

	va_start(args, format);
	while (*format)
	{
		if (*format != '%')
		{
			_putchar(*format);
			count++;
		}
		else if (*format == '%' && *(format + 1) == '%')
		{
			format++;
			_putchar('%');
			count++;
		}
		else if (*format == '%' && *(format + 1) != '%')
		{
			format++;
			function = get_func(*format);
			if (*(format) == '\0')
				return (-1);
			else if (function == NULL)
			{
				_putchar(*(format - 1));
				_putchar(*format);
				count += 2;
			}
			else
				count += function(args);
		}
		format++;
	}
	va_end(args);
	return (count);
}
