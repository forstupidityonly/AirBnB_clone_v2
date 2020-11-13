#include "holberton.h"
/**
  * get_func - selects correct function for format spec
  * @specifier: the format char
  * Return: function ptr to correct function
  */
int (*get_func(char specifier))(va_list)
{
	int itr = 0;
	function_select opt[] = {
		{'c', select_c},
		{'s', select_s},
		{'i', select_i},
		{'d', select_i},
		{'b', select_b},
		{'R', select_R},
		{'r', select_r},
		{'u', select_u},
		{'\0', NULL}
	};

	while (opt[itr].specifier)
	{
		if (opt[itr].specifier == specifier)
			return (opt[itr].function);
		itr++;
	}
	return (NULL);
}
