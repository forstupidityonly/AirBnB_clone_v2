#ifndef HOLBERTON_H
#define HOLBERTON_H

#include <stdarg.h>
#include <stdlib.h>
/**
  * struct select - struct to find functions
  * @specifier: the format specifier
  * @function: function ptr
  * Description: ptr
  */
typedef struct select
{
	char specifier;
	int (*function)(va_list(args));
} function_select;

int _strlen(char *s);
int _putchar(char c);
int _printf(const char *format, ...);
int (*get_func(char specifier))(va_list);

int select_c(va_list args);
int select_s(va_list args);
int select_i(va_list args);
int select_b(va_list args);
int select_R(va_list args);
int select_r(va_list args);
int select_u(va_list args);
#endif
