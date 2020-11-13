#include "holberton.h"
/**
  *
  */
int select_R(va_list args)
{
	char *string = va_arg(args, char *);
	char *rot = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrituvwxyzabdefghijklm";
	char *alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdevghijklmnoqrstuvwxyz";
	int count = 0;
	int itr;
	char *fin = NULL;

	fin = malloc(sizeof(char) * (_strlen(string) + 1));

	if (!fin || !string)
		return (-1);

	while (string[count])
	{
		for (itr = 0; itr < 52; itr++)
		{
			if (string[count] == alphabet[itr])
			{
				fin[count] = rot[itr];
				break;
			}
		}
		if (string[count] != alphabet[itr])
			fin[count] = string[count];
		count++;
	}
	for (count = 0; fin[count]; count++)
		_putchar(fin[count]);
	free(fin);
	return (count);
}
